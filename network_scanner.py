import scapy.all as scapy
import optparse

# arp request
# broadcast
# response


def get_user_input():
    po = optparse.OptionParser()
    po.add_option("-i", "--ip_address", dest="ip", help="enter ip address")
    (user_input, arguments) = po.parse_args()
    if not user_input.ip:
        print("enter ip address")
    return user_input


def scan_network(ip):
    arp_request = scapy.ARP(pdst=ip)
    # scp.ls(scp.ARP())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scp.ls(scp.Ether))
    merged_packet = broadcast/arp_request
    (answered_list, unanswered_list) = scapy.srp(merged_packet, timeout=1)
    #  if an ip don't answer we won't wait until we get an answer.
    answered_list.summary()


user_ip_address = get_user_input()
scan_network(user_ip_address.ip)

"""
for al in list(answered_list):
    print(al)
    print('\n\n')
"""