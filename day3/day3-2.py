list = []
with open("day3-input.txt", "r") as f:
    for line in f:
        list.append(line.strip("\n"))
width = len(list[0])
product = 1

def getTrees(xSlope, ySlope):
    global product
    treeCounter = 0
    xCounter = 0
    for line in list[::ySlope]:
        if line[xCounter] == '#':
            treeCounter += 1
        xCounter += xSlope
        if xCounter >= width:
            xCounter -= width
    product *= treeCounter

getTrees(1, 1)
getTrees(3, 1)
getTrees(5, 1)
getTrees(7, 1)
getTrees(1, 2)

print(product)


    
