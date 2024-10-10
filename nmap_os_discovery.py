# OS discvoery script
import time
start = time.time()
import nmap

nm = nmap.PortScanner()
# host = '10.10.10.75'  # my laptop
host = '10.10.10.24'  # my mobile
nm.scan(host, arguments='-O', sudo=True)

# show all results for the target
for host in nm.all_hosts():
    print(f"IP: {host}")
    if (os_info := nm[host].get('osmatch')):
        print(f"OS info: {os_info}")
    else:
        print("No OS info found")
print(f"Time taken: {time.time() - start} seconds")