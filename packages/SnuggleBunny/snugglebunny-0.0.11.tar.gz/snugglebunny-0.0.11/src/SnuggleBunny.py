import argparse
import ipaddress
import re
import socket
import ssl
from clear import clear

CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"

def SnuggleBunny():
    clear()
    parser = argparse.ArgumentParser()
    parser.add_argument("-host", required = True)
    parser.add_argument("-port", default = 443)
    parser.add_argument("-filename", default = "")
    args = parser.parse_args()
    
    hosts = []
    if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}", args.host):
        for i in list(ipaddress.ip_network(args.host, strict = False).hosts()):
            hosts.append(str(i))

    else:
        hosts.append(args.host)
        
    hits = []
    for host in hosts:
        print(f"{CYAN}CHECKING: {host}")

        # DNS
        dns = socket.getfqdn(host)
        if dns != host:
            hits.append(f"DNS: {dns}")
            print(f"{GREEN}DNS: {dns}")

        # SSL SOCKETS
        context = ssl.create_default_context()
        ciphers = context.get_ciphers()
        for cipher in ciphers:
            try:
                new_context = ssl.create_default_context()
                new_context.set_ciphers(cipher["name"])
                new_context.check_hostname = False
                new_context.verify_mode = ssl.CERT_NONE
                socket.setdefaulttimeout(10)
                with socket.create_connection((host, args.port)) as sock:
                    with new_context.wrap_socket(sock, server_hostname = host) as secure_sock:
                        if "DES" in cipher["name"] or "EXP" in cipher["name"] or "MD5" in cipher["name"] or "NULL" in cipher["name"] or "RC4" in cipher["name"]:
                            if cipher["strength_bits"] < 128:
                                hits.append(f"OFFERS WEAK CIPHER and STRENGTH | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")
                                print(f"{RED}OFFERS WEAK CIPHER AND STRENGTH | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")

                            elif cipher["protocol"] != "TLSv1.2" and cipher["protocol"] != "TLSv1.3":
                                hits.append(f"OFFERS WEAK CIPHER AND PROTOCOL | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")
                                print(f"{ORANGE}OFFERS WEAK CIPHER AND PROTOCOL  | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")

                            elif cipher["strength_bits"] < 128 and cipher["protocol"] != "TLSv1.2" and cipher["protocol"] != "TLSv1.3":
                                hits.append(f"OFFERS WEAK CIPHER, PROTOCOL, AND STRENGTH | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")
                                print(f"{RED}OFFERS WEAK CIPHER, PROTOCOL, AND STRENGTH | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")
                                
                            else:
                                hits.append(f"OFFERS WEAK CIPHER | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")
                                print(f"{RED}OFFERS WEAK CIPHER | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")

                        elif cipher["strength_bits"] < 128:
                            hits.append(f"OFFERS WEAK STRENGTH | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")
                            print(f"{RED}OFFERS WEAK STRENGTH | {cipher['name']} | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")

                        elif cipher["protocol"] != "TLSv1.2" and cipher["protocol"] != "TLSv1.3":
                            hits.append(f"OFFERS WEAK PROTOCOL | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")
                            print(f"{YELLOW}OFFERS WEAK PROTOCOL | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")

                        elif cipher["strength_bits"] < 128 and cipher["protocol"] != "TLSv1.2" and cipher["protocol"] != "TLSv1.3":
                            hits.append(f"OFFERS WEAK PROTOCOL AND STRENGTH | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")
                            print(f"{RED}OFFERS WEAK PROTOCOL AND STRENGTH | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")

                        else:
                            hits.append(f"OFFERS STRONG CIPHER, PROTOCOL, AND STRENGTH  | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")
                            print(f"{GREEN}OFFERS STRONG CIPHER, PROTOCOL, AND STRENGTH | CIPHER = {cipher['name']} | PROTOCOL = {cipher['protocol']} | STRENGTH = {cipher['strength_bits']} bits")

            except:
                pass

    if len(args.filename) > 0:
        with open(f"{args.filename}.txt", "w") as file:
            for hit in hits:
                file.write(hit)

    print(f"{CYAN}DONE!")

if __name__ == "__main__":
    SnuggleBunny()
