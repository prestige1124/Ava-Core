# Scan system for vulnerabilities

 
import psutil
import platform

# This module scans the system for vulnerabilities by collecting information about CPU usage, memory usage, disk usage, platform, and running processes. It uses the psutil library to gather this information and returns it in a structured format.
# The run method collects the relevant data and returns it as a dictionary, which can then be used for further analysis or reporting. This module can be extended in the future to include more detailed vulnerability scanning and analysis based on the collected system information.
# TODO: Implement more detailed vulnerability scanning based on the collected system information, such as checking for known vulnerabilities in running processes, analyzing system configurations, and providing recommendations for improving security.
class SystemScan:


    def run(self):
        data = {}

        data['cpu_percent'] = psutil.cpu_percent(interval=1)
        data['memory_percent'] = psutil.virtual_memory().percent
        data['disk_percent'] = psutil.disk_usage('/').percent   
        data['platform'] = platform.system()
        data['processes'] = []
        

        process = []
        for proc in psutil.process_iter(['pid', 'name']):
            process.append(proc.info)

        data['processes'] = process

        return data              