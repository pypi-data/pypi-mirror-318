import re

from scapy.layers.inet import TCP, IP
from scapy.packet import Raw

from xbase_util.xbase_constant import plain_content_type_columns, packetKeyname, src_dst_header, statisticHeader, \
    features_key, plain_body_columns
from xbase_util.xbase_util import firstOrZero


def content_type_is_plain(packet):
    """
    从单个包（包括header和body）中获取content-type并判断是否为可见类型
    :param packet:
    :return:
    """
    if ":" not in packet:
        return False
    for item in packet.replace("-", "_").replace(" ", "").lower().split("\n"):
        if "content_type" in item:
            if ":" not in item:
                continue
            content_type = item.split(":")[1].replace("\r", "").strip()
            return content_type in plain_content_type_columns
    return False


def filter_visible_chars(data):
    """
    过滤不可见字符，仅保留可打印的ASCII字符
    :param data:
    :return:
    """
    return ''.join(chr(b) for b in data if 32 <= b <= 126 or b in (9, 10, 13))


def get_all_columns(
        contains_packet_column=False,
        contains_src_dst_column=False,
        contains_statistic_column=False,
        contains_features_column=False,
        contains_plain_body_column=False,
        contains_pcap_flow_text=False
):
    result_columns = []
    if contains_packet_column:
        result_columns += packetKeyname
    if contains_src_dst_column:
        result_columns += src_dst_header
    if contains_statistic_column:
        result_columns += statisticHeader
    if contains_features_column:
        result_columns += features_key
    if contains_plain_body_column:
        result_columns += plain_body_columns
    if contains_pcap_flow_text:
        result_columns.append(contains_pcap_flow_text)
    return result_columns


req_pattern = re.compile(r"(GET|POST|HEAD|PUT|DELETE|OPTIONS|PATCH) \/[^\s]* HTTP\/\d\.\d[\s\S]*?\r\n\r\n",
                         re.DOTALL)
res_pattern = re.compile(r"HTTP/\d\.\d \d{3}.*", re.DOTALL)
req_body_pattern = re.compile(
    r"(GET|POST|HEAD|PUT|DELETE|OPTIONS|PATCH) \/[^\s]* HTTP\/\d\.\d[\s\S]*?(?=HTTP/\d\.\d)", re.DOTALL)


def get_all_packets_by_reg(packets):
    http_Req_Raw = {}
    http_methods = ("POST /", "PUT /", "OPTIONS /", "DELETE /", "GET /")
    for packet in packets:
        if TCP in packet and Raw in packet:
            data = packet[Raw].load
            ack = packet[TCP].ack
            next_ack = packet[TCP].seq + len(data)
            if ack not in http_Req_Raw:
                http_Req_Raw[ack] = {"time": [packet.time], "data": data, "next_ack": next_ack}
            else:
                http_Req_Raw[ack]["time"].append(packet.time)
                http_Req_Raw[ack]["data"] += data
                http_Req_Raw[ack]["next_ack"] = next_ack
    packet_list = [
        {
            'req_data': item['data'],
            'res_data': http_Req_Raw[item['next_ack']]['data'],
            'req_text': filter_visible_chars(item['data']),
            'res_text': filter_visible_chars(http_Req_Raw[item['next_ack']]['data']),
            'req_time': item['time'],
            'res_time': http_Req_Raw[item['next_ack']]['time']
        }
        for ack, item in http_Req_Raw.items()
        if any(method in filter_visible_chars(item['data']) for method in http_methods)
    ]
    return packet_list
# def get_all_packets_by_reg(packets):
#     packets = [packet for packet in packets if packet.haslayer(TCP) and packet.haslayer(IP) and packet.haslayer(Raw)]
#     packet_list = []
#     my_map = {
#         'req_data': b'',
#         'res_data': b'',
#         'req_text': '',
#         'res_text': '',
#         'req_time': [],
#         'res_time': []
#     }
#     last_is_req = None
#     for item in packets:
#         data = item[Raw].load
#         time = float(item.time)
#         req_match = req_pattern.search(filter_visible_chars(data))
#         res_match = res_pattern.search(filter_visible_chars(data))
#         if req_match is not None or res_match is not None:
#             if req_match:
#                 # 新的请求：请求时间不为空或者响应时间不为空，说明不为空，添加到列表并清空数据
#                 if len(my_map['req_time']) != 0 or len(my_map['res_time']) != 0:
#                     packet_list.append(my_map.copy())
#                 my_map = {
#                     'req_data': data,
#                     'res_data': b'',
#                     'req_text': filter_visible_chars(data),
#                     'res_text': '',
#                     'req_time': [time],
#                     'res_time': []
#                 }
#                 last_is_req = True
#             if res_match:
#                 my_map['res_data'] += data
#                 my_map['res_text'] = filter_visible_chars(my_map['res_data'])
#                 my_map['res_time'].append(time)
#                 last_is_req = False
#         else:
#             # 不是请求不是相应，就是中间的包
#             if last_is_req is None:
#                 # 一开始就没匹配到请求或者响应头，那就不管即使是中间的包
#                 continue
#             if last_is_req is True:
#                 my_map['req_time'].append(time)
#                 my_map['req_data'] += data
#                 my_map['req_text'] = filter_visible_chars(my_map['req_data'])
#             elif last_is_req is False:
#                 my_map['res_time'].append(time)
#                 my_map['res_data'] += data
#                 my_map['res_text'] = filter_visible_chars(my_map['res_data'])
#     if len(my_map['req_time']) != 0 or len(my_map['res_time']) != 0:
#         packet_list.append(my_map.copy())
#     return packet_list


def get_body(param):
    body = "".join([item.strip() for item in param.split("\r\n\r\n") if item.strip() != "" and "HTTP/" not in param])
    return "" if body is None else body


def get_header_value(header_set, value):
    result = [item for item in header_set if value in item]
    if len(result) != 0:
        return result[0].replace(f"{value}:", "").strip()
    else:
        return ""


def get_detail_by_package(packets_from_pcap, publicField, use_regx):
    """
    通过pcap的数量分离session并完善相关字段
    :param packets_from_pcap: 通过PcAp解析出的包
    :param publicField: 原始的session单条数据
    :return: 完整的单条数据
    """
    res_field = publicField.copy()
    if use_regx:
        req = packets_from_pcap['req_text']
        res = packets_from_pcap['res_text']
    else:
        res = packets_from_pcap["response"]
        req = packets_from_pcap["request"]
    res_field["initRTT"] = firstOrZero(res_field.get("initRTT", 0))
    res_field["length"] = firstOrZero(res_field.get("length", 0))
    request_lines = req.strip().split("\n")
    http_request_lines = [item for item in request_lines if "HTTP" in item]
    if len(http_request_lines) != 0:
        first_line = http_request_lines[0].split(" ")
        res_field['http.clientVersion'] = str(first_line[2]).replace("\n", "").replace("\r", "")
        res_field['http.path'] = first_line[1]
        res_field['http.method'] = first_line[0]
    else:
        res_field['http.clientVersion'] = ''
        res_field['http.path'] = ''
        res_field['http.method'] = ''
    res_field['http.request-referer'] = get_header_value(header_set=request_lines, value="Referer")
    res_field['http.request-content-type'] = get_header_value(header_set=request_lines,
                                                              value="Content-Type")
    res_field['http.hostTokens'] = get_header_value(header_set=request_lines, value="Host")

    if use_regx:
        res_field['plain_body_src'] = ""
        res_field['plain_body_dst'] = ""
        if content_type_is_plain(req):
            res_field['plain_body_src'] = get_body(req)
        if content_type_is_plain(res):
            res_field['plain_body_dst'] = get_body(res)

    response_lines = res.strip().split("\n")
    http_response_lines = [item for item in response_lines if "HTTP" in item]
    if len(http_response_lines) != 0:
        first_line = http_response_lines[0].strip().split(" ")
        res_field['http.statuscode'] = first_line[1]
        res_field['http.serverVersion'] = first_line[0].split("/")[1]
    else:
        res_field['http.statuscode'] = ""
        res_field['http.serverVersion'] = ""
    res_field['http.response-server'] = get_header_value(header_set=response_lines, value="Server")
    res_field['http.response-content-type'] = get_header_value(header_set=response_lines,
                                                               value="Content-Type")
    for response in list(set(response_lines + request_lines)):
        key_value = response.replace("\r", "").split(":")
        if len(key_value) == 2:
            key = key_value[0].replace(" ", "").replace("-", "_").lower()
            value = key_value[1].replace(" ", "")
            if f"src_{key}" in src_dst_header:
                res_field[f"src_{key}"] = value
            if f"dst_{key}" in src_dst_header:
                res_field[f"dst_{key}"] = value
    return res_field
