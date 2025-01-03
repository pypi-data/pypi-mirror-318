import copy
import re

import numpy as np
from scapy.all import *
from scapy.layers.inet import TCP

REQUEST_LINE_RE = re.compile(rb"^(GET|POST|PUT|DELETE|OPTIONS|HEAD|PATCH)\s[^\r\n]+\r\n", re.MULTILINE)
RESPONSE_LINE_RE = re.compile(rb"^HTTP/\d\.\d\s+\d{3}\s?[^\r\n]*", re.IGNORECASE)


def read_packets(packets):
    last_seq_len = -1
    last_ack = -1
    packet_list = []
    tmp_data = b''
    tmp_packets = []
    for index, pkt in enumerate(packets):
        data = pkt[Raw].load if Raw in pkt else b''
        ack = pkt[TCP].ack
        seq = pkt[TCP].seq
        if seq == last_seq_len:
            # print(f"检测到连续包 数据长度:{len(data)} + seq:{seq}={len(data) + seq}  ack:{ack}")
            tmp_data += data
            tmp_packets.append(pkt)
        elif seq == last_ack:
            if tmp_data != b'':
                if REQUEST_LINE_RE.match(tmp_data) or RESPONSE_LINE_RE.match(tmp_data):
                    packet_list.append({'data': copy.deepcopy(tmp_data), 'pkts': copy.deepcopy(tmp_packets)})
                else:
                    # print("没有新的请求或者响应，就把数据加到上一个里面")
                    if len(packet_list) > 0:
                        # 之前找到过有请求，可以添加到之前的数据，否则说明一开始就没找到请求
                        packet_list[-1]['pkts'].extend(copy.deepcopy(tmp_packets))
                        packet_list[-1]['data'] += tmp_data

            tmp_data = data
            tmp_packets = [pkt]
            # print(f"顺序正确 数据长度:{len(data)} + seq:{seq}={len(data) + seq}  ack:{ack}")
        else:
            # print(f"顺序错误 数据长度:{len(data)} + seq:{seq}={len(data) + seq}  ack:{ack}")
            if len(data) > 0:
                # 但是有数据
                tmp_data += data
                tmp_packets.append(pkt)
        last_ack = ack
        last_seq_len = seq + len(data)
    if tmp_data != b'':
        packet_list.append({'data': copy.deepcopy(tmp_data), 'pkts': copy.deepcopy(tmp_packets)})
        tmp_packets.clear()
    return packet_list


def parse_req_or_res(data, pkts):
    if data.find(b"\r\n\r\n") != -1:
        res = data.split(b"\r\n\r\n", 1)
        header = res[0]
        body = res[1]
    else:
        header = data
        body = b''
    pattern_chuncked = re.compile(rb"Transfer-Encoding:\s*chunked", re.IGNORECASE)
    pattern_gzip = re.compile(rb"Content-Encoding:\s*gzip", re.IGNORECASE)
    chuncked_pattern = pattern_chuncked.search(header)
    gzip_pattern = pattern_gzip.search(header)
    if chuncked_pattern and b'chunked' in chuncked_pattern.group():
        chunk_lines = [item for item in body.split(b"\r\n") if item != b'']
        data = b''
        next_chunk_size = 0
        for chunk in chunk_lines:
            try:
                next_chunk_size = int(chunk, 16)
                if next_chunk_size == 0:
                    break
                # print(f"接下来的分段大小：{next_chunk_size}")
            except:
                if next_chunk_size > 0:
                    data += chunk
                    # print(f"分段数据大小：{len(data)}")
        result_body = data
    else:
        # print("虽然没有指定chunked，但是我猜出来他就是chunked")
        if body.endswith(b"0\r\n"):
            chunk_lines = [item for item in body.split(b"\r\n") if item != b'']
            data = b''
            next_chunk_size = 0
            for chunk in chunk_lines:
                try:
                    next_chunk_size = int(chunk, 16)
                    if next_chunk_size == 0:
                        break
                    # print(f"接下来的分段大小：{next_chunk_size}")
                except:
                    if next_chunk_size > 0:
                        data += chunk
                        # print(f"分段数据大小：{len(data)}")
            result_body = data
        else:
            result_body = body
    if gzip_pattern and b'gzip' in gzip_pattern.group():
        try:
            decompressed = gzip.decompress(result_body)
            result_body_str = "\n".join(
                [line.strip() for line in decompressed.decode("utf-8", errors="replace").splitlines() if
                 line.strip() != ""])
        except Exception as e:
            result_body_str = result_body.decode("utf-8", errors="replace")
    else:
        result_body_str = result_body.decode("utf-8", errors="replace")
    return header.decode("utf-8", errors="replace"), result_body_str, [float(pkt.time) for pkt in pkts]


def get_all_packets_by_segment(packets):
    res = read_packets(packets)
    request_packets = [item for item in res if REQUEST_LINE_RE.match(item['data'])]
    response_packets = [
        {'first_seq': item['pkts'][0][TCP].seq, 'pkts': item['pkts'], 'first_ack': item['pkts'][0][TCP].ack,
         'data': item['data']} for item in
        res if RESPONSE_LINE_RE.match(item['data'])]
    packet_list = []
    for request in request_packets:
        pkt_list = request['pkts']
        last_pkt = pkt_list[-1]
        # seq = last_pkt[TCP].seq
        ack = last_pkt[TCP].ack
        response = [item for item in response_packets if item['first_seq'] == ack]
        # print(f"找到对应的响应：{len(response)}")
        # print(f"请求：{request['data'].decode('utf-8', errors='replace')}")
        if len(response) > 0:
            res_header, res_body, res_times = parse_req_or_res(response[0]['data'], response[0]['pkts'])
            req_header, req_body, req_times = parse_req_or_res(request['data'], request['pkts'])
            packet_list.append({
                "req_header": req_header,
                "req_body": req_body,
                "req_time": req_times,
                "req_packets": len(request['pkts']),
                "res_header": res_header,
                "res_body": res_body,
                "res_time": res_times,
                "res_packets": len(response[0]['pkts']),
            })
        else:
            # print("没响应")
            req_header, req_body, req_times = parse_req_or_res(request['data'], request['pkts'])
            packet_list.append({
                "req_header": req_header,
                "req_body": req_body,
                "req_time": req_times,
                "req_packets": len(request['pkts']),
                "res_header": '',
                "res_body": '',
                "res_time": [],
                "res_packets": 0,
            })
    return packet_list


# if __name__ == '__main__':
    # all_packets = get_all_packets_by_segment(rdpcap("../out/3post.pcap"))
    # res=[
    #     get_detail_by_package({}, package['req_header'], package['req_body'], package['res_header'],
    #                           package['req_body']) for package in all_packets]
    # print(res)