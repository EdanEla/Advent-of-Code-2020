solution = 0
list = []
with open("day1-input.txt", "r") as f:
    for line in f:
        list.append(int(line.strip("\n")))
for i in list:
    subList = list[list.index(i):len(list)]
    for j in subList:
        subSubList = subList[subList.index(j):len(subList)]
        for z in subSubList:
            if i + j + z == 2020:
                solution = i * j * z
                break
        if solution != 0:
            break
    if solution != 0:
        break

print(solution)
        
