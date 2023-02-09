The nmap library provides a more comprehensive and efficient way to scan ports compared to using raw sockets.
In this code, we create an instance of the nmap.PortScanner class and use the scan method to scan the specified host and ports.
The state of each port can be checked by accessing the state property of the tcp dictionary.

This implementation is more efficient and provides more functionality than the previous implementation, but it also requires installing the nmap library. You can install it by running pip install python-nmap in your terminal.
