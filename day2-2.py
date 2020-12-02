list = []
with open("day2-input.txt", "r") as f:
    for line in f:
        list.append(line.strip("\n"))
solution = 0
for password in list:
    policy = password.split(":")[0]
    letters = (password.split(":")[1]).strip(" ")
    character = policy[len(policy) - 1]
    countLetters = 0
    bounds = policy.split(" ")[0]
    index1 = int(bounds.split("-")[0])
    index2 = int(bounds.split("-")[1])
    

    for i in range(0, len(letters)):
        if i + 1 == index2 and letters[i] == character:
            solution += 1
            break
        elif i + 1 == index1 and letters[i] == character:
            if letters[index2 - 1] != character:
                solution += 1
            else:
                break
                
    
print(solution)


