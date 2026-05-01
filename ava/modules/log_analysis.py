# Analyze logs for failed logins and other security events

import re


# This module analyzes log files for security events such as failed logins and sudo attempts. It reads the specified log file, searches for relevant patterns using regular expressions, and counts the occurrences of these events. The analyze method returns a dictionary with the counts of failed logins and sudo attempts, which can be used for further analysis or reporting.
# TODO: Extend the log analysis to include more types of security events, such as successful logins, unauthorized access attempts, and other relevant patterns. Additionally, consider implementing a more robust log parsing mechanism that can handle different log formats and provide more detailed insights into the security events.
# Note: The current implementation assumes a specific log format and may need adjustments to work with different types of log files or formats.
class LogAnalysis:

    def analyze(self, logfile=r"C:\Users\jbrew\Documents\fake_auth.log.log"):
        
        failed_logins = 0
        sudo_attempts = 0

        try:
            with open(logfile, 'r') as f:
                for line in f:
                    if re.search(r'Failed password', line):
                        failed_logins += 1
                    if re.search(r'sudo', line):
                        sudo_attempts += 1
                    if re.search(r'authentication failure', line):
                        failed_logins += 1

        except FileNotFoundError:
            print(f"Log file {logfile} not found.")
            return None

        return {'failed_logins': failed_logins, 'sudo_attempts': sudo_attempts}
