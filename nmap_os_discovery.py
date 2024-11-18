# OS discvoery script
import time
start = time.time()
import nmap

nmap_scanner = nmap.PortScanner()
host = '10.10.10.75'  # my laptop
# host = '10.10.10.24'  # my mobile
# host = '3.123.143.202'  # gadi
nmap_scanner.scan(host, arguments='-O', sudo=True)

# show all results for the target
for host in nmap_scanner.all_hosts():
    print(f"IP: {host}")

    os_info = nmap_scanner[host].get('osmatch')
    
    if not os_info:
        print("No OS info found")
        continue

    for i, os in enumerate(os_info):
        print(f"OS Match #{i + 1}")
        print(f"Name: {os.get('name')}")
        print(f"Accuracy: {os.get('accuracy')}%")
        print(f"Type: {os.get('osclass')[0].get('type')}")
        print(f"Vendor: {os.get('osclass')[0].get('vendor')}")
        print(f"Family: {os.get('osclass')[0].get('osfamily')}")
        print(f"Generation: {os.get('osclass')[0].get('osgen')}")
        print(f"Device Type: {os.get('osclass')[0].get('devicetype')}")
        print(f"CPE: {os.get('osclass')[0].get('cpe')}")
        print()
print(f"Time taken: {round(time.time() - start, 2)} seconds")