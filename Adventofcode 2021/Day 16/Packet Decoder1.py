from struct import pack
import sys
sys.path.insert(0, '.')
from tools import log


LITERAL = "100"

class Literal():
    def __init__(self, version, id, bytes):
        self.version = version
        self.id = id
        self.bytes = bytes
        self.sub_packets = []

    def __repr__(self) -> str:
        return str(int(self.bytes, 2))#wunderschön

class Packet():
    def __init__(self,version,id,len_t_id,sub_packets):
        self.version = version
        self.id = id
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
    the_sum = int(packet.version, 2)
    for p in packet.sub_packets:
        the_sum += version_sum(p)
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