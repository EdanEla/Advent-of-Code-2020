inputs = [0]
with open("day10-input.txt", "r") as f:
    for line in f:
        inputs.append(int(line.strip("\n")))

def sort(i):
    if inputs[i] > inputs[i + 1]:
        var = inputs[i + 1]
        inputs[i + 1] = inputs[i]
        inputs[i] = var

for j in range(0, len(inputs)):
    for i in range(0, len(inputs) - 1):
        sort(i)
inputs.append(inputs[len(inputs) - 1] + 3)

counter1 = 0
counter3 = 0
for i in range(0, len(inputs) - 1):
    if inputs[i + 1] - inputs[i] == 1:
        counter1 += 1
    elif inputs[i + 1] - inputs[i] == 3:
        counter3 += 1
print(counter1 * counter3)
        
    
