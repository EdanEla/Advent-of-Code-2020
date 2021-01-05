with open("day13-input.txt", "r") as f:
        timeStamp = int(f.readline())
        IDList = f.readline().split(',')

soonestDepart = 99999
soonestDepartID = 0
for ID in IDList:
    if ID != "x":
        ID = int(ID)
        if ID - timeStamp % ID < soonestDepart:
            soonestDepart = ID - timeStamp % ID
            soonestDepartID = ID
print(soonestDepart * soonestDepartID)
