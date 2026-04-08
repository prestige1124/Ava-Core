
#
# Ava - An AI Virtual Assistant
# Core module   
from ava.modules.conversation import ConversationModule


# Ava class that serves as the main interface for the virtual assistant
# It initializes the conversation module and provides methods for greeting and processing commands.
# The process method takes a command as input and returns the response from the conversation module.
class Ava:

    def __init__(self):
        self.conversation = ConversationModule()

    # TODO: Add diffrent greetings based on time of day, user preferences, etc.
    #     - Morning: "Good morning! How can I assist you today?"
    #     - Afternoon: "Good afternoon! What can I do for you?"
    #     - Evening: "Good evening! How can I help you tonight?"
    def greet(self):
        return "Hello, I am Ava version 0.4. How can I protect your system?"
    
    def process(self, command):

        if command == "scan system":
            from ava.modules.system_scan import SystemScan
            system_scan = SystemScan()
            return system_scan.run()
        
        if command == "analyze logs":
            from ava.modules.log_analysis import LogAnalysis
            log_analysis = LogAnalysis()
            return log_analysis.analyze()


        # netwrok

        if command == "scan network":
            from ava.modules.network_scan import NetworkScanner
            network_scanner = NetworkScanner()
            network_scanner.scan_ports()
            return network_scanner.get_open_ports()

        # reporting 



        return self.conversation.respond(command)