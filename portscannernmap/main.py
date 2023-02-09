import nmap

def scan_ports(host, ports):
    nm = nmap.PortScanner()
    nm.scan(host, str(ports))
    open_ports = []
    for port in ports:
        if nm[host]['tcp'][port]['state'] == 'open':
            open_ports.append(port)
    return open_ports

host = input("Enter the host to scan: ")
ports = [21, 22, 23, 80, 443, 8080]
open_ports = scan_ports(host, ports)

print("Open ports on host " + host + ": ")
print(open_ports)
