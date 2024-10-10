import nmap
import json

nm = nmap.PortScanner()
nm.scan('3.123.143.202', arguments='-A -p-')

with open('nmap0_output.txt', 'w') as f:
    f.write(json.dumps(nm.scaninfo()))