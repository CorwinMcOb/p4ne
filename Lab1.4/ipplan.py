from ipaddress import IPv4Network
import random

random.seed()

# random.randint(0x0b000000, 0xdf000000)

# random.randint(8, 24)

# net1 = ipaddress.IPv4Network((random.randint(0x0b000000, 0xdf000000), random.randint(8, 24)), strict=False)

# print(net1)

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        IPv4Network.__init__(self, (random.randint(0x0b000000, 0xdf000000), random.randint(8, 24)), strict=False)

    def regular(self):
        if self.is_global:
            return self.is_global
        else:
            return False

    def key_value(self):
        return int(self.network_address)+int(self.netmask)

def sortfunc(x):
    return x.key_value()

random_network_list = []

for i in range(0, 51):
    random_network = IPv4RandomNetwork()
    if random_network.regular() and random_network not in random_network_list:
        random_network_list.append(random_network)
    # print(IPv4RandomNetwork())

for j in sorted(random_network_list, key=sortfunc):
    print(j)