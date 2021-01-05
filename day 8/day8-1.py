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
    instruction = inputs[line][0:3]
    argument = inputs[line].split(" ")[1]
    if i in linesRead:
        print(accumulator)
        return None
    linesRead.append(i)
    if instruction == "nop":
        i += 1
        if i < len(inputs):
            followInstruction(i)
    elif instruction == "acc":
        if argument[0] == "+":
            accumulator += int(argument[1:])
        else:
            accumulator -= int(argument[1:])
        i += 1
        if i < len(inputs):
            followInstruction(i)
    elif instruction == "jmp":
        if argument[0] == "+":
            i += int(argument[1:])
        else:
            i -= int(argument[1:])
        followInstruction(i)

followInstruction(0)
