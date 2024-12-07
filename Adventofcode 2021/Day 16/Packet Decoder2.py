from struct import pack
import sys

from numpy import multiply
sys.path.insert(0, '.')
from tools import log


LITERAL = "100"

class Literal():
    def __init__(self, version, id, bytes):
        self.version = version
        self.id = id
        self.bytes = bytes
        self.value = int(bytes, 2)
        self.sub_packets = []

    def __repr__(self) -> str:
        return str(self.value)#wunderschön

class Packet():
    def __init__(self,version,id,len_t_id,sub_packets):
        self.value = 0
        self.version = int(version, 2)
        self.id = int(id, 2)
        self.len_t_id = len_t_id
        self.sub_packets = sub_packets
    
    def __repr__(self) -> str:
        return str([self.version,self.id,self.len_t_id,self.sub_packets])

def new_packet(data):
    version = data[:3]
    id = data[3:6]
    len_t_id, sub_packets, bits = get_subpackets(data)

    return Literal(version,id,"".join(sub_packets)) if len_t_id == None else Packet(version,id,len_t_id,sub_packets), bits

def version_sum(packet):
    the_sum = packet.value
    packets = []
    for p in packet.sub_packets:
        packets.append(version_sum(p))

    if packet.id == 0:#sum
        the_sum = sum(packets)

    elif packet.id == 1:#product
        the_sum = 1
        for x in packets:
            the_sum *= x

    elif packet.id == 2:#min
        the_sum = min(packets)      
    elif packet.id == 3:#max
        the_sum = max(packets)
    elif packet.id == 5:#grater than
        the_sum = 1 if packets[0] > packets[1] else 0
    elif packet.id == 6:#less than
        the_sum = 1 if packets[0] < packets[1] else 0
    elif packet.id == 7:#equal
        the_sum = 1 if packets[0] == packets[1] else 0

    return the_sum

def get_subpackets(packet):
    sub_packets = []
    if packet[3:6] == LITERAL:
        for x in range(6, len(packet), 5):
            sub_packets.append(packet[x+1:x+5])

            if packet[x] == "0":
                break
        return (None, sub_packets, packet[x+5:])
    else:
        len_t_id = int(packet[6])
        if len_t_id == 0:
            length = int(packet[7:22], 2)
            bits = packet[22:22+length]
            while bits:
                subs, bits = new_packet(bits)
                sub_packets.append(subs)
            packet = packet[22+length:]

        else:
            length = int(packet[7:18], 2)
            packet = packet[18:]
            for i in range(length):
                subs, bits = new_packet(packet)
                sub_packets.append(subs)
                packet = bits
        return (len_t_id, sub_packets, packet)



def parse_data(data):
    return data

def hex_to_bin(hex_str):
    not_completed_bin = str(bin(int(hex_str,16))).removeprefix("0b")
    while len(not_completed_bin)/4 != len(hex_str):
        not_completed_bin = "0" + not_completed_bin 
    return not_completed_bin



@log
def main(data):
    data = parse_data(data)
    
    #print(hex_to_bin(data))

    return version_sum(new_packet(hex_to_bin(data))[0])

data1 = open("./Day 16/data1", "r").read()
data2 = open("./Day 16/data2", "r").read()

main(data1)
main(data2)