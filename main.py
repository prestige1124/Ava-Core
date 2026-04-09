from ava.core import Ava

assistant = Ava()

print(assistant.greet())

while True:
    command = input("Enter a command (or 'exit' to quit): ")
    if command.lower() == 'exit':
        print("Safe travels!")
        break
    response = assistant.process(command)
    print(response)