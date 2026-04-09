# Conversation module for Ava
# This module handles basic conversational interactions with the user.
# The respond method takes a text input and returns a response based on the content of the text.

class ConversationModule:

    def respond(self, text):
        text = text.lower()

        #TODO: decide, will conversation module handle all interactions, or just basic ones, and pass more complex ones to other modules? 
        # For now, just basic ones. If not, put conversation in core and have it route to other modules as needed.


        #TODO: Implement more complex conversation handling, including natural language processing, context awareness, and personalized responses based on user preferences and history.
        if "hello" in text:
            return "Hello user and hello world!"

        #TODO: add more status checks, such as CPU usage, memory usage, disk space, etc.       
        if "status" in text:
            return "Systems fully operational."
        
        return "I do not recognize that command"