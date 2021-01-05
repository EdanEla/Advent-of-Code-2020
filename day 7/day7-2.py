inputs = []
with open("day7-input.txt", "r") as f:
    for line in f:
        inputs.append(line.strip(".\n"))

def getBag(x):
    bag = x.split("contain ")[0]
    return bag[:len(bag) - 6]

def getNextBags(x):
    global depth
    global multiplier
    global solution
    depth += 1
    nextBags = x.split("contain ")[1].split(', ')
    for bag in nextBags:
        if len(nextBags) > 1 and nextBags[len(nextBags)-1] != bag:
            splitDepth.append(depth)
        if bag[0] == 'n':
            if (len(splitDepth) > 0):
                for i in range(0, depth - splitDepth[len(splitDepth) - 1]):
                    multipliers.pop()
                multiplier = 1
                for mult in multipliers:
                    multiplier *= mult
                depth = splitDepth[len(splitDepth) - 1]
                splitDepth.pop()
            break
        multiplier *= int(bag[0])
        lastMultiplier = int(bag[0])
        solution += multiplier
        multipliers.append(lastMultiplier)
        if "bags" in bag:
            bag = bag[2:len(bag) - 5]
        else:
            bag = bag[2:len(bag) - 4]
        for line in inputs:
            if bag == getBag(line):
                getNextBags(line)

for z in inputs:
    if getBag(z) == "shiny gold":
        line = z

multiplier = 1
depth = 0
splitDepth = []
multipliers = []
depth = 0
i = 0
solution = 0

getNextBags(line)
print(solution)
