list = []
with open("day2-input.txt", "r") as f:
    for line in f:
        list.append(line.strip("\n"))
solution = 0
for password in list:
    policy = password.split(":")[0]
    letters = password.split(":")[1]
    character = policy[len(policy) - 1]
    countLetters = 0
    bounds = policy.split(" ")[0]
    lowerBound = int(bounds.split("-")[0])
    upperBound = int(bounds.split("-")[1])

    for char in letters:
        if char == character:
            countLetters += 1
    if countLetters >= lowerBound and countLetters <= upperBound:
        solution += 1
print(solution)


