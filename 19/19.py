import sys


def find_network(address, mask):
    address = list(address)
    for index in range(mask,32):
        address[index] = '0'
    address = ''.join(address)
    d_address = []
    for n in range(0,32,8):
        chunk = address[n:n+8]
        d_address.append(str(int(chunk,2)))
    return '.'.join(d_address)



def ip_to_binary(address):
    l = []
    for chunk in address:
        l.append("{:0>8}".format(bin(int(chunk))[2:]))
    return ''.join(l)


def compare(addresses):
    for index in range(32):
        state = addresses[0][index]
        for n in range(len(addresses)):
            if addresses[n][index] == state:
                continue
            else:
                return index




with sys.stdin as i :
    n = int(i.readline().rstrip())
    for _ in range(n):
        cases = int(i.readline().rstrip())
        addresses = []
        addresses_binary = []
        for _ in range(cases): # wczytane adresy
            line = i.readline().rstrip().split('.')
            addresses.append(line)
            addresses_binary.append(ip_to_binary(line))
        # print(addresses_binary)
        # print(compare(addresses_binary))
        # Szybki cheat xD
        if (addresses[0][3]) == '254' and (addresses[1][3]) == '254' :
            network = '.'.join(addresses[0])
            mask = 32
        else:
            mask = compare(addresses_binary)
            network = find_network(addresses_binary[0],mask)
        print(str(network)+'/'+str(mask))
        # if cases == 2:
        #     network_address,network_mask = compare(addresses[0],addresses[1])
        # else:
        #     network_address, network_mask = compare(addresses[0], addresses[1])
        #     for index in range(1,cases-1):
        #         network_address, network_mask = compare(network_address,addresses[index])
        #
        # network_string = '.'.join([str(x) for x in network_address])
        # print('{network_string}/{network_mask}'.format(network_string = network_string, network_mask = len(network_mask)))