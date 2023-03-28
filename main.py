import re


def get_ip():
    my_ip = str(input('Put Your Ip: '))
    subnet_mask = str(input('Put Your Subnet Mask: '))
    regex_ip = r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b'
    if re.search(regex_ip, my_ip) and re.search(regex_ip, subnet_mask):
        binary_ip(my_ip, subnet_mask)
    else:
        print('Ip Not Found!!!')
    return 0


def binary_ip(ip, subnet):
    my_ip_binary = ''
    subnet_mask_binary = ''
    ip_list = list(map(int, ip.split('.')))
    subnet_list = list(map(int, subnet.split('.')))
    for i in ip_list:
        my_ip_binary += str(bin(i)[2:].zfill(8))
    for i in subnet_list:
        subnet_mask_binary += str(bin(i)[2:].zfill(8))
    net_and_broadcast_id(my_ip_binary, subnet_mask_binary)
    host_id(my_ip_binary, subnet_mask_binary)
    return 0


def net_and_broadcast_id(ip, subnet):
    subnet_0 = subnet.count('0')
    ip_list = list(ip)
    broadcast_list = list(ip)
    for i in range(1, subnet_0 + 1):
        ip_list[-i] = '0'
        broadcast_list[-i] = '1'
    net_id = "".join(ip_list)
    net_id = str(int(net_id[:8], 2)) + "." + str(int(net_id[8:16], 2)) + "." + str(int(net_id[16:24], 2)) + "." + str(
        int(net_id[24:32], 2))
    broadcast_id = "".join(broadcast_list)
    broadcast_id = str(int(broadcast_id[:8], 2)) + "." + str(int(broadcast_id[8:16], 2)) + "." + str(
        int(broadcast_id[16:24], 2)) + "." + str(int(broadcast_id[24:32], 2))
    print('Net Id = ', net_id)
    print('Broadcast Id = ', broadcast_id)
    return 0


def host_id(ip, subnet):
    subnet_0 = subnet.count('1')
    ip_list = list(ip)
    for i in range(subnet_0):
        ip_list[i] = '0'
    host_id = "".join(ip_list)
    host_id = str(int(host_id[:8], 2)) + "." + str(int(host_id[8:16], 2)) + "." + str(
        int(host_id[16:24], 2)) + "." + str(int(host_id[24:32], 2))
    print('Host Id = ', host_id)
    return 0


get_ip()


