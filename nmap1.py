import time
start = time.time()
import nmap
import json

nm = nmap.PortScanner()
# nm.scan('3.123.143.0/24', arguments='-sn', sudo=False)
nm.scan('10.10.10.0/24', arguments='-sn', sudo=True) if 1 else ""

for host in nm.all_hosts():
    print(f"IP: {host}, name: {nm[host].hostname()}")
    # exit()
print(f"{len(nm.all_hosts())} hosts up")
print(f"Time taken: {time.time() - start} seconds")