inputs = []
with open("day9-input.txt", "r") as f:
    for line in f:
        inputs.append(line.strip("\n"))


for index in range(25, len(inputs)):
    count = 0
    for i in range(1, 26):
        for j in range(1, 26):
            if int(inputs[index - i]) + int(inputs[index - j]) == int(inputs[index]) and i != j:
                count += 1
    if count == 0:
        invalid = int(inputs[index])


def nextNumber(i, j):
    global total
    global end
    global solution
    global candidates
    if total + int(inputs[j]) == invalid:
        end = True
        candidates.append(int(inputs[j]))
        solution = candidates
        return None
    else:
        candidates.append(int(inputs[j]))
        total += int(inputs[j])
        if len(inputs) > j + 1:
            nextNumber(i, j + 1)

solution = []
end = False
for i in range(0, len(inputs)):
    if end == True:
        break
    total = int(inputs[i])
    candidates = [int(inputs[i])]
    for j in range(i + 1,len(inputs)):
        if total + int(inputs[j]) == invalid:
            end = True
            candidates.append(int(inputs[j]))
            solution = candidates
            break
        else:
            candidates.append(int(inputs[j]))
            total += int(inputs[j])
        #candidates = [int(inputs[i])]
        #total = int(inputs[i])

highestValue = 0
lowestValue = 999999999
for value in solution:
    if value > highestValue:
        highestValue = value
    if value < lowestValue:
        lowestValue = value
print(highestValue + lowestValue)
        
                
        
        
