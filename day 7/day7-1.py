inputs = []
with open("day7-input.txt", "r") as f:
    for line in f:
        inputs.append(line.strip(".\n"))

def getBag(x):
    bag = x.split("contain ")[0]
    return bag[:len(bag) - 6]

def getNextBags(x):
    nextBags = x.split("contain ")[1].split(', ')
    for bag in nextBags:
        global end
        if end == True:
            break
        if "bags" in bag:
            bag = bag[2:len(bag) - 5]
        else:
            bag = bag[2:len(bag) - 4]
        if "shiny gold" == bag:
            global count
            count += 1
            end = True
            break;
        else:
            for line in inputs:
                if bag == getBag(line):
                    getNextBags(line)
            
count = 0
lineCounter = 1
for line in inputs:
    print(lineCounter)
    lineCounter += 1
    global end
    end = False
    getNextBags(line)
print(count)
