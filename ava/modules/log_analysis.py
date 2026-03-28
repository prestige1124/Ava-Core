# Analyze logs for failed logins and other security events

import re

class LogAnalysis:

    def analyze(self, logfile=r"C:\Users\jbrew\OneDrive\Documents\fake_auth.log.log"):
        
        failed_logins = 0
        sudo_attempts = 0

        try:
            with open(logfile, 'r') as f:
                for line in f:
                    if re.search(r'Failed password', line):
                        failed_logins += 1
                    if re.search(r'sudo', line):
                        sudo_attempts += 1

        except FileNotFoundError:
            print(f"Log file {logfile} not found.")
            return None

        return {'failed_logins': failed_logins, 'sudo_attempts': sudo_attempts}
