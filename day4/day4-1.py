list = [[]]
i = 0
with open("day4-input.txt", "r") as f:
    for line in f:
        if line == "\n":
            list.append([])
            i += 1
        else:
            list[i] += line.strip("\n").split(" ")
        
        
#print(list)
counter = 0
for line in list:
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    presentFields = []
    for i in range(0, len(line)):
        presentFields.append(line[i].split(":")[0])
    for i in presentFields:
        for j in fields:
            if i == j:
                fields.remove(j)
    if fields == [] or fields == ["cid"]:
        counter += 1
print(counter)
        
    
