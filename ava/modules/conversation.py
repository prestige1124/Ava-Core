
#

class ConversationModule:

    def respond(self, text):
        text = text.lower()

        if "hello" in text:
            return "Hello Jake and hello world!"
        
        if "status" in text:
            return "Systems fully operational."
        
        return "I do not recognize that command"