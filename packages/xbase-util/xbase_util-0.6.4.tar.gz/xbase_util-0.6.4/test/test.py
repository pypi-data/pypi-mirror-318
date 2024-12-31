from scapy.utils import rdpcap

from xbase_util.packet_util import get_all_packets_by_reg, get_body

if __name__ == '__main__':
    p = get_all_packets_by_reg(rdpcap("t1.pcap"))
    for packet in p:
        print( packet['req_text'])
        print(get_body(packet,is_req=True))