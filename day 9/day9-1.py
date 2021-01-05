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
        print(inputs[index])
                
        
        
