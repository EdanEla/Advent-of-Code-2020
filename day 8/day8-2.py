inputs = []
with open("day8-input.txt", "r") as f:
    for line in f:
        inputs.append(line.strip(".\n"))


i = 0
accumulator = 0
linesRead = []
def followInstruction(line):
    global i
    global accumulator
    global linesRead
    global j
    if line >= len(inputs):
        print(accumulator)
        return None
    instruction = inputs[line][0:3]
    argument = inputs[line].split(" ")[1]
    if i in linesRead:
        return None
    linesRead.append(i)
    if instruction == "nop":
        i += 1
        if i < len(inputs):
            followInstruction(i)
        else:
            return None
    elif instruction == "acc":
        if argument[0] == "+":
            accumulator += int(argument[1:])
        else:
            accumulator -= int(argument[1:])
        i += 1
        if i < len(inputs):
            followInstruction(i)
        else:
            return None
    elif instruction == "jmp":
        if argument[0] == "+":
            i += int(argument[1:])
        else:
            i -= int(argument[1:])
        followInstruction(i)


for j in range(0, len(inputs)):
    i = 0
    accumulator = 0
    linesRead = []
    if inputs[j][0:3] == "nop":
        inputs[j] = "jmp" + " " + inputs[j].split(" ")[1]
        followInstruction(0)
        inputs[j] = "nop" + " " + inputs[j].split(" ")[1]
    elif inputs[j][0:3] == "jmp":
        inputs[j] = "nop" + " " + inputs[j].split(" ")[1]
        followInstruction(0)
        inputs[j] = "jmp" + " " + inputs[j].split(" ")[1]

