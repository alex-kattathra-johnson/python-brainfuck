class Interpreter(object):

    def __init__(self, text):
        self.badcode = False
        self.code = self.clean_code(list(text))
        self.braces = self.bracemap(self.code)

    def run(self):
        machine, codeindex, mindex = [0], 0, 0
        str_list = []
        while codeindex < len(self.code):
            if len(self.code) == 0 or self.badcode:
                return "Please enter valid code!"
            cmd = self.code[codeindex]
            if cmd == "+":
                machine[mindex] = machine[mindex] + 1 if machine[mindex] < 255 else 0
            if cmd == "-":
                machine[mindex] = machine[mindex] - 1 if machine[mindex] > 0 else 255
            if cmd == ">":
                mindex += 1
                if mindex == len(machine): machine.append(0)
            if cmd == "<":
                mindex = 0 if mindex <=0 else mindex - 1
            if cmd == ".":
                str_list.append(chr(machine[mindex]))
            if cmd == ",":
                input_char = raw_input('Input an ASCII character for position ' + str(mindex) + "\n")
                if len(input_char) == 0:
                    return ''.join(str_list)
                while len(input_char) != 1:
                    input_char = raw_input('Please input a valid ASCII character for position ' + str(mindex) + "\n")
                while ord(list(input_char)[0]) > 255 or ord(list(input_char)[0]) <= 0:
                    input_char = raw_input('Please input a valid ASCII character for position ' + str(mindex) + "\n")
                machine[mindex] = ord(input_char)
            if cmd == "[" and machine[mindex] == 0:
                codeindex = self.braces[codeindex]
            if cmd == "]" and machine[mindex] != 0:
                codeindex = self.braces[codeindex]
            codeindex += 1
        return ''.join(str_list)

    def error(self):
        raise Exception('Error parsing input')

    def clean_code(self, code):
        return list(filter(lambda x: x in ['+', '-', '>', '<', '.', ',', '[', ']'], code))

    def bracemap(self, code):
        tempstack, result = [], {}
        for i, char in enumerate(code):
            if char == "[":
                tempstack.append(i)
            if char == "]":
                startpos = tempstack.pop();
                result[startpos] = i;
                result[i] = startpos;
        if len(tempstack) != 0:
            self.badcode = True
        return result
