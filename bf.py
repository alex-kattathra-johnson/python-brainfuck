import sys
from interpreter import Interpreter
import readline


def main():
    while True:
        try:
            text = raw_input('bf> ')
        except EOFError:
            break
        if not text:
            continue
        if text == "exit":
            print("Exiting...")
            sys.exit(0);
        interpreter = Interpreter(text)
        result = interpreter.run()
        print(result)


if __name__ == '__main__':
    main()
