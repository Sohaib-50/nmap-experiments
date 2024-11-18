# ports and trace route discovery 
import time
start = time.time()
import nmap

nmap_scanner = nmap.PortScanner()
# host = '10.10.10.75'  # my laptop
# host = '10.10.10.24'  # my mobile
host = '3.123.143.202'  # gadi
nmap_scanner.scan(host, arguments='-O -p- -traceroute', sudo=True)

for host in nmap_scanner.all_hosts():
    print(f"IP: {host}\n")

    # OS
    os_info = nmap_scanner[host].get('osmatch')
    if not os_info:
        print("No OS info found")
    else:
        print(f"{len(os_info)} OS matches found")
        print(f"{'Name':<20}{'Accuracy':<10}{'Type':<10}{'Vendor':<15}{'Family':<15}{'Generation':<15}{'Device Type':<15}{'CPE':<30}")
        print("-" * 148)
        for i, os in enumerate(os_info):
            os_class = os.get('osclass', [{}])[0]
            cpe = ', '.join(os_class.get('cpe', [])) if isinstance(os_class.get('cpe', []), list) else os_class.get('cpe', '')
            print(f"{str(os.get('name', '')):<20}{str(os.get('accuracy', '')):<10}{str(os_class.get('type', '')):<10}{str(os_class.get('vendor', '')):<15}{str(os_class.get('osfamily', '')):<15}{str(os_class.get('osgen', '')):<15}{str(os_class.get('devicetype', '')):<15}{str(cpe):<30}")
        print()
    
    # Ports
    all_ports = {
        **nmap_scanner[host].get('tcp', {}),
        **nmap_scanner[host].get('udp', {}),
        **nmap_scanner[host].get('sctp', {})
    }
    print(f"{len(all_ports)} ports found")
    print(f"{'Port':<8}{'State':<10}{'Service':<15}{'Product':<20}{'Version':<10}{'Confidence':<10}")
    print("-" * 73)
    for port, port_info in all_ports.items():
        print(f"{port:<8}{str(port_info.get('state', '')):<10}{str(port_info.get('name', '')):<15}{str(port_info.get('product', '')):<20}{str(port_info.get('version', '')):<10}{str(port_info.get('conf', '')):<10}")
    print()

    # Trace route
    trace_route = nmap_scanner[host].get('traceroute', [])
    print(f"{len(trace_route)} hops found")
    print(f"{'Hop #':<8}{'IP':<20}{'RTT':<10}{'Host':<20}")
    print("-" * 58)
    for i, hop in enumerate(trace_route):
        print(f"{i + 1:<8}{str(hop.get('ip', '')):<20}{str(hop.get('rtt', '')):<10}{str(hop.get('host', '')):<20}")
    print()

print(f"Time taken: {round(time.time() - start, 2)} seconds")