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


steps = [1]
for i in range(1, len(inputs)):
    steps.append(0)
    for j in range(1, 4):
        if i - j >= 0 and inputs[i] - inputs[i - j] <= 3:
            steps[i] += steps[i - j]
print(steps[len(inputs) - 1])



