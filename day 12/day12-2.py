inputs = []
with open("day12-input.txt", "r") as f:
    for line in f:
        inputs.append(line.strip("\n"))

nsDistance = 1
ewDistance = 10
rotation = 0
ship = [0, 0]
for i in inputs:
    direction = i[0]
    amount = int(i[1:])
    
    if direction == "F":
        ship[0] += ewDistance * amount
        ship[1] += nsDistance * amount
    if direction == "N":
        nsDistance += amount
    elif direction == "S":
        nsDistance -= amount
    elif direction == "E":
        ewDistance += amount
    elif direction == "W":
        ewDistance -= amount
    elif direction == "R":
        rotation = int(amount/90)
        while rotation > 0:
            extra = ewDistance
            ewDistance = nsDistance
            nsDistance = extra * -1
            rotation -= 1
    elif direction == "L":
        rotation = int(amount/90)
        while rotation > 0:
            extra = nsDistance
            nsDistance = ewDistance
            ewDistance = extra * -1
            rotation -= 1

if ship[0] < 0:
    ship[0] *= -1
if ship[1] < 0:
    ship[1] *= -1
print(ship[0] + ship[1])

