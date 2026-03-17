

from ava.core import Ava

def main():
    ava = Ava()
    print(ava.greet())

    while True:
        command = input(">> ")

        if command == "exit":
            break

        response = ava.process(command)
        print(response)

if __name__ == "__main__":
    main()

