
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

    def greet(self):
        return "Hello, I am Ava version 0.1"
    
    def process(self, command):




        return self.conversation.respond(command)