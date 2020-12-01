list = []
solution = 0
with open("day1-input.txt", "r") as f:
    for line in f:
        list.append(int(line.strip("\n")))
for i in list:
    subList = list[list.index(i):len(list)]
    for j in subList:
        if i + j == 2020:
            solution = i * j
            break
    if solution > 0:
        break
print(solution)
        
