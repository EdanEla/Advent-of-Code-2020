inputs = []
with open("day12-input.txt", "r") as f:
    for line in f:
        inputs.append(line.strip("\n"))

nsDistance = 0
ewDistance = 0
rotation = 0
directions = ["E", "S", "W", "N"]
for i in inputs:
    direction = i[0]
    amount = int(i[1:])
    
    if direction == "F":
        direction = directions[rotation]
    if direction == "N":
        nsDistance += amount
    elif direction == "S":
        nsDistance -= amount
    elif direction == "E":
        ewDistance += amount
    elif direction == "W":
        ewDistance -= amount
    elif direction == "R":
        rotation += int(amount/90)
        if rotation > 3:
            rotation -= 4
    elif direction == "L":
        rotation -= int(amount/90)
        if rotation < 0:
            rotation += 4

if nsDistance < 0:
    nsDistance *= -1
if ewDistance < 0:
    ewDistance *= -1

print(nsDistance + ewDistance)

