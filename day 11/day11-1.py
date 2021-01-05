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
            if j - 1 >= 0 and seats[i][j - 1] == "#":
                occupied += 1
            elif j + 1 < len(seats[i]) and seats[i][j + 1] == "#":
                occupied += 1
            elif i + 1 < len(seats) and j - 1 >= 0 and seats[i + 1][j - 1] == "#":
                occupied += 1
            elif i + 1 < len(seats) and seats[i + 1][j] == "#":
                occupied += 1
            elif i + 1 < len(seats) and j + 1 < len(seats[i]) and seats[i + 1][j + 1] == "#":
                occupied += 1
            elif i - 1 >= 0 and j - 1 >= 0 and seats[i - 1][j - 1] == "#":
                occupied += 1
            elif i - 1 >= 0 and seats[i - 1][j] == "#":
                occupied += 1
            elif i - 1 >= 0 and j + 1 < len(seats[i]) and seats[i - 1][j + 1] == "#":
                occupied += 1
            if occupied == 0:
                newSeats[i] = newSeats[i][:j] + "#" + newSeats[i][j + 1:]
        if seats[i][j] == "#":
            occupied = 0
            if j - 1 >= 0 and seats[i][j - 1] == "#":
                occupied += 1
            if j + 1 < len(seats[i]) and seats[i][j + 1] == "#":
                occupied += 1
            if i + 1 < len(seats) and j - 1 >= 0 and seats[i + 1][j - 1] == "#":
                occupied += 1
            if i + 1 < len(seats) and seats[i + 1][j] == "#":
                occupied += 1
            if i + 1 < len(seats) and j + 1 < len(seats[i]) and seats[i + 1][j + 1] == "#":
                occupied += 1
            if i - 1 >= 0 and j - 1 >= 0 and seats[i - 1][j - 1] == "#":
                occupied += 1
            if i - 1 >= 0 and seats[i - 1][j] == "#":
                occupied += 1
            if i - 1 >= 0 and j + 1 < len(seats[i]) and seats[i - 1][j + 1] == "#":
                occupied += 1
            if occupied >= 4:
                newSeats[i] = newSeats[i][:j] + "L" + newSeats[i][j + 1:]
x = 0
while seats != newSeats:
    for i in range(0, len(newSeats)):
        seats[i] = newSeats[i]
    for i in range(0, len(seats)):
        for j in range(0, len(seats[i])):
            if seats[i][j] == "L":
                occupied = 0
                if j - 1 >= 0 and seats[i][j - 1] == "#":
                    occupied += 1
                elif j + 1 < len(seats[i]) and seats[i][j + 1] == "#":
                    occupied += 1
                elif i + 1 < len(seats) and j - 1 >= 0 and seats[i + 1][j - 1] == "#":
                    occupied += 1
                elif i + 1 < len(seats) and seats[i + 1][j] == "#":
                    occupied += 1
                elif i + 1 < len(seats) and j + 1 < len(seats[i]) and seats[i + 1][j + 1] == "#":
                    occupied += 1
                elif i - 1 >= 0 and j - 1 >= 0 and seats[i - 1][j - 1] == "#":
                    occupied += 1
                elif i - 1 >= 0 and seats[i - 1][j] == "#":
                    occupied += 1
                elif i - 1 >= 0 and j + 1 < len(seats[i]) and seats[i - 1][j + 1] == "#":
                    occupied += 1
                if occupied == 0:
                    newSeats[i] = newSeats[i][:j] + "#" + newSeats[i][j + 1:]
            if seats[i][j] == "#":
                occupied = 0
                if j - 1 >= 0 and seats[i][j - 1] == "#":
                    occupied += 1
                if j + 1 < len(seats[i]) and seats[i][j + 1] == "#":
                    occupied += 1
                if i + 1 < len(seats) and j - 1 >= 0 and seats[i + 1][j - 1] == "#":
                    occupied += 1
                if i + 1 < len(seats) and seats[i + 1][j] == "#":
                    occupied += 1
                if i + 1 < len(seats) and j + 1 < len(seats[i]) and seats[i + 1][j + 1] == "#":
                    occupied += 1
                if i - 1 >= 0 and j - 1 >= 0 and seats[i - 1][j - 1] == "#":
                    occupied += 1
                if i - 1 >= 0 and seats[i - 1][j] == "#":
                    occupied += 1
                if i - 1 >= 0 and j + 1 < len(seats[i]) and seats[i - 1][j + 1] == "#":
                    occupied += 1
                if occupied >= 4:
                    newSeats[i] = newSeats[i][:j] + "L" + newSeats[i][j + 1:]
    x += 1

counter = 0
for i in newSeats:
    for j in i:
        if j == "#":
            counter += 1
print(counter)
        
    
