inputs = [[]]
i = 0
with open("day6-input.txt", "r") as f:
    for line in f:
        if line == "\n":
            inputs.append([])
            i += 1
        else:
            inputs[i] += line.strip("\n")
alphabet= [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
sum = 0
for group in inputs:
    counter = 0
    for letter in alphabet:
        if letter in group:
            counter += 1
    sum += counter
print(sum)


    
