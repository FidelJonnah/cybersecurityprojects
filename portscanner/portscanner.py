import socket

def is_port_open(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((host, int(port)))
        s.shutdown(2)
        return True
    except:
        return False

def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        if is_port_open(host, port):
            open_ports.append(port)
    return open_ports

host = input("Enter the host to scan: ")
ports = [21, 22, 23, 80, 443, 8080]
open_ports = scan_ports(host, ports)

print("Open ports on host " + host + ": ")
print(open_ports)
