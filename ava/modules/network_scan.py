# Scan network for open ports 

import psutil

class NetworkScanner:
    def __init__(self):
        self.open_ports = []

    def scan_ports(self):
        # Get all network connections
        connections = psutil.net_connections()
        
        for conn in connections:
            if conn.status == 'LISTEN' and conn.laddr.port not in self.open_ports:
                self.open_ports.append(conn.laddr.port)

    def get_open_ports(self):
        return self.open_ports
    
    