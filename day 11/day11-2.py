inputs = []
with open("day11-input.txt", "r") as f:
    for line in f:
        inputs.append(line.strip("\n"))

seats = inputs
newSeats = []
for i in seats:
    newSeats.append(i)


for i in range(0, len(seats)):
    for j in range(0, len(seats[i])):
        if seats[i][j] == "L":
            occupied = 0
            z = 0
#left
            while True:
                if j - 1 - z < 0:
                    break
                if seats[i][j - 1 - z] == "#":
                    occupied += 1
                    break
                elif seats[i][j - 1 - z] == "L":
                    break
#right                
                z += 1
            z = 0
            while True:
                if j + 1 + z >= len(seats[i]):
                    break
                if seats[i][j + 1 + z] == "#":
                    occupied += 1
                    break
                elif seats[i][j + 1 + z] == "L":
                    break
                z += 1
            z = 0
#left-down
            while True:
                if i + 1 + z >= len(seats) or j - 1 - z < 0:
                    break
                if seats[i + 1 + z][j - 1 - z] == "#":
                    occupied += 1
                    break
                elif seats[i + 1 + z][j - 1 - z] == "L":
                    break
                z += 1
            z = 0
#down
            while True:
                if i + 1 + z >= len(seats):
                    break
                if seats[i + 1 + z][j] == "#":
                    occupied += 1
                    break
                elif seats[i + 1 + z][j] == "L":
                    break
                z += 1
            z = 0
#down-right
            while True:
                if i + 1 + z >= len(seats) or j + 1 + z >= len(seats[i]):
                    break
                if seats[i + 1 + z][j + 1 + z] == "#":
                    occupied += 1
                    break
                elif seats[i + 1 + z][j + 1 + z] == "L":
                    break
                z += 1
            z = 0
#up-left
            while True:
                if i - 1 - z < 0 or j - 1 - z <0:
                    break
                if seats[i - 1- z][j - 1 - z] == "#":
                    occupied += 1
                    break
                elif seats[i - 1- z][j - 1 - z] == "L":
                    break
                z += 1
            z = 0
#up
            while True:
                if i - 1 - z < 0:
                    break
                if seats[i - 1 - z][j] == "#":
                    occupied += 1
                    break
                elif seats[i - 1 - z][j] == "L":
                    break
                z += 1
            z = 0
#up-right
            while True:
                if i - 1 - z < 0 or j + 1 + z >= len(seats[i]):
                    break
                if seats[i - 1 - z][j + 1 + z] == "#":
                    occupied += 1
                    break
                elif seats[i - 1 - z][j + 1 + z] == "L":
                    break
                z += 1
            z = 0
            if occupied == 0:
                newSeats[i] = newSeats[i][:j] + "#" + newSeats[i][j + 1:]
#occupation
        if seats[i][j] == "#":
            occupied = 0
            z = 0
#left
            while True:
                if j - 1 - z < 0:
                    break
                if seats[i][j - 1 - z] == "#":
                    occupied += 1
                    break
                elif seats[i][j - 1 - z] == "L":
                    break
#right                
                z += 1
            z = 0
            while True:
                if j + 1 + z >= len(seats[i]):
                    break
                if seats[i][j + 1 + z] == "#":
                    occupied += 1
                    break
                elif seats[i][j + 1 + z] == "L":
                    break
                z += 1
            z = 0
#left-down
            while True:
                if i + 1 + z >= len(seats) or j - 1 - z < 0:
                    break
                if seats[i + 1 + z][j - 1 - z] == "#":
                    occupied += 1
                    break
                elif seats[i + 1 + z][j - 1 - z] == "L":
                    break
                z += 1
            z = 0
#down
            while True:
                if i + 1 + z >= len(seats):
                    break
                if seats[i + 1 + z][j] == "#":
                    occupied += 1
                    break
                elif seats[i + 1 + z][j] == "L":
                    break
                z += 1
            z = 0
#down-right
            while True:
                if i + 1 + z >= len(seats) or j + 1 + z >= len(seats[i]):
                    break
                if seats[i + 1 + z][j + 1 + z] == "#":
                    occupied += 1
                    break
                elif seats[i + 1 + z][j + 1 + z] == "L":
                    break
                z += 1
            z = 0
#up-left
            while True:
                if i - 1 - z < 0 or j - 1 - z <0:
                    break
                if seats[i - 1- z][j - 1 - z] == "#":
                    occupied += 1
                    break
                elif seats[i - 1- z][j - 1 - z] == "L":
                    break
                z += 1
            z = 0
#up
            while True:
                if i - 1 - z < 0:
                    break
                if seats[i - 1 - z][j] == "#":
                    occupied += 1
                    break
                elif seats[i - 1 - z][j] == "L":
                    break
                z += 1
            z = 0
#up-right
            while True:
                if i - 1 - z < 0 or j + 1 + z >= len(seats[i]):
                    break
                if seats[i - 1 - z][j + 1 + z] == "#":
                    occupied += 1
                    break
                elif seats[i - 1 - z][j + 1 + z] == "L":
                    break
                z += 1
            z = 0
            if occupied >= 5:
                newSeats[i] = newSeats[i][:j] + "L" + newSeats[i][j + 1:]



x = 0
while seats != newSeats:
    for i in range(0, len(newSeats)):
        seats[i] = newSeats[i]
    for i in range(0, len(seats)):
        for j in range(0, len(seats[i])):
            if seats[i][j] == "L":
                occupied = 0
                z = 0
    #left
                while True:
                    if j - 1 - z < 0:
                        break
                    if seats[i][j - 1 - z] == "#":
                        occupied += 1
                        break
                    elif seats[i][j - 1 - z] == "L":
                        break
    #right                
                    z += 1
                z = 0
                while True:
                    if j + 1 + z >= len(seats[i]):
                        break
                    if seats[i][j + 1 + z] == "#":
                        occupied += 1
                        break
                    elif seats[i][j + 1 + z] == "L":
                        break
                    z += 1
                z = 0
    #left-down
                while True:
                    if i + 1 + z >= len(seats) or j - 1 - z < 0:
                        break
                    if seats[i + 1 + z][j - 1 - z] == "#":
                        occupied += 1
                        break
                    elif seats[i + 1 + z][j - 1 - z] == "L":
                        break
                    z += 1
                z = 0
    #down
                while True:
                    if i + 1 + z >= len(seats):
                        break
                    if seats[i + 1 + z][j] == "#":
                        occupied += 1
                        break
                    elif seats[i + 1 + z][j] == "L":
                        break
                    z += 1
                z = 0
    #down-right
                while True:
                    if i + 1 + z >= len(seats) or j + 1 + z >= len(seats[i]):
                        break
                    if seats[i + 1 + z][j + 1 + z] == "#":
                        occupied += 1
                        break
                    elif seats[i + 1 + z][j + 1 + z] == "L":
                        break
                    z += 1
                z = 0
    #up-left
                while True:
                    if i - 1 - z < 0 or j - 1 - z <0:
                        break
                    if seats[i - 1- z][j - 1 - z] == "#":
                        occupied += 1
                        break
                    elif seats[i - 1- z][j - 1 - z] == "L":
                        break
                    z += 1
                z = 0
    #up
                while True:
                    if i - 1 - z < 0:
                        break
                    if seats[i - 1 - z][j] == "#":
                        occupied += 1
                        break
                    elif seats[i - 1 - z][j] == "L":
                        break
                    z += 1
                z = 0
    #up-right
                while True:
                    if i - 1 - z < 0 or j + 1 + z >= len(seats[i]):
                        break
                    if seats[i - 1 - z][j + 1 + z] == "#":
                        occupied += 1
                        break
                    elif seats[i - 1 - z][j + 1 + z] == "L":
                        break
                    z += 1
                z = 0
                if occupied == 0:
                    newSeats[i] = newSeats[i][:j] + "#" + newSeats[i][j + 1:]
    #occupation
            if seats[i][j] == "#":
                occupied = 0
                z = 0
    #left
                while True:
                    if j - 1 - z < 0:
                        break
                    if seats[i][j - 1 - z] == "#":
                        occupied += 1
                        break
                    elif seats[i][j - 1 - z] == "L":
                        break
    #right                
                    z += 1
                z = 0
                while True:
                    if j + 1 + z >= len(seats[i]):
                        break
                    if seats[i][j + 1 + z] == "#":
                        occupied += 1
                        break
                    elif seats[i][j + 1 + z] == "L":
                        break
                    z += 1
                z = 0
    #left-down
                while True:
                    if i + 1 + z >= len(seats) or j - 1 - z < 0:
                        break
                    if seats[i + 1 + z][j - 1 - z] == "#":
                        occupied += 1
                        break
                    elif seats[i + 1 + z][j - 1 - z] == "L":
                        break
                    z += 1
                z = 0
    #down
                while True:
                    if i + 1 + z >= len(seats):
                        break
                    if seats[i + 1 + z][j] == "#":
                        occupied += 1
                        break
                    elif seats[i + 1 + z][j] == "L":
                        break
                    z += 1
                z = 0
    #down-right
                while True:
                    if i + 1 + z >= len(seats) or j + 1 + z >= len(seats[i]):
                        break
                    if seats[i + 1 + z][j + 1 + z] == "#":
                        occupied += 1
                        break
                    elif seats[i + 1 + z][j + 1 + z] == "L":
                        break
                    z += 1
                z = 0
    #up-left
                while True:
                    if i - 1 - z < 0 or j - 1 - z <0:
                        break
                    if seats[i - 1- z][j - 1 - z] == "#":
                        occupied += 1
                        break
                    elif seats[i - 1- z][j - 1 - z] == "L":
                        break
                    z += 1
                z = 0
    #up
                while True:
                    if i - 1 - z < 0:
                        break
                    if seats[i - 1 - z][j] == "#":
                        occupied += 1
                        break
                    elif seats[i - 1 - z][j] == "L":
                        break
                    z += 1
                z = 0
    #up-right
                while True:
                    if i - 1 - z < 0 or j + 1 + z >= len(seats[i]):
                        break
                    if seats[i - 1 - z][j + 1 + z] == "#":
                        occupied += 1
                        break
                    elif seats[i - 1 - z][j + 1 + z] == "L":
                        break
                    z += 1
                z = 0
                if occupied >= 5:
                    newSeats[i] = newSeats[i][:j] + "L" + newSeats[i][j + 1:]
    x += 1

counter = 0
for i in newSeats:
    for j in i:
        if j == "#":
            counter += 1
print(counter)
        
