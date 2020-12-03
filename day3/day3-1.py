list = []
with open("day3-input.txt", "r") as f:
    for line in f:
        list.append(line.strip("\n"))
bottom = len(list)
width = len(list[0])
xCounter = 0
treeCounter = 0
for line in list:
    if line[xCounter] == '#':
        treeCounter += 1
    xCounter += 3
    if xCounter >= width:
        xCounter -= width

print(treeCounter)
    
