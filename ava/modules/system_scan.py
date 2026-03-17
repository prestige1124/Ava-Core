

#

import psutil
import platform


class SystemScan:


    def run(self):
        data = {}

        data['cpu_percent'] = psutil.cpu_percent(interval=1)
        data['memory_percent'] = psutil.virtual_memory().percent
        data['disk_percent'] = psutil.disk_usage('/').percent   
        data['platform'] = platform.system()

        process = []
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            process.append(proc.info)

        data['processes'] = process

        return data              