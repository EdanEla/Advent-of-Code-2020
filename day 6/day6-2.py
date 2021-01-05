inputs = [[]]

i = 0
with open("day6-input.txt", "r") as f:
    for line in f:
        if line == "\n":
            inputs.append([])
            i += 1
        else:
            inputs[i].append(line.strip("\n"))


count = 0
for group in inputs:
    alphabet= [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
    for person in group:
        answers = []
        for letter in alphabet:
            if letter not in person:
                answers.append(letter)
        for letter in answers:
            alphabet.remove(letter)
    for letter in alphabet:
        count += 1
print(count)


    
