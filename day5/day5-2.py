inputs = []
with open("day5-input.txt", "r") as f:
    for line in f:
        inputs.append(line.strip("\n"))
highestSeatID = 0
seatIDs = []
for line in inputs:
    rows = list(range(0, 128))
    columns = list(range(0, 8))
    for char in line:
        if char == "F":
            rows = rows[:int(len(rows)/2)]
        elif char == "B":
            rows = rows[int(len(rows)/2):]
        elif char == "L":
            columns = columns[:int(len(columns)/2)]
        elif char == "R":
            columns = columns[int(len(columns)/2):]
    seatID = rows[0] * 8 + columns[0]
    seatIDs.append(seatID)

for i in range(0, 218 * 8 + 8):
    if (i not in seatIDs) and (i + 1 in seatIDs) and (i - 1 in seatIDs):
        print(i)
        break


