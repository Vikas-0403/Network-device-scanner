from scapy.all import ARP, Ether, srp # type: ignore

def scan(ip_range):
    # Create ARP request
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # Send packet and get response
    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def display(devices):
    print("IP" + " "*18 + "MAC")
    print("-"*40)
    for device in devices:
        print(f"{device['ip']:20} {device['mac']}")

if __name__ == "__main__":
    target_range = input("Enter IP range (e.g. 192.168.1.1/24): ")
    scanned = scan(target_range)
    display(scanned)
