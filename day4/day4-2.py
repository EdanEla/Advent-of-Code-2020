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
        presentFields.append(line[i].split(":"))
    for i in presentFields:
        for j in fields:
            if i[0] == j:
                string = i[1]
                if i[0] == "byr":
                    if int(string) >= 1920 and int(string) <= 2002:
                        fields.remove(j)
                    break
                elif i[0] == "iyr":
                        if int(string) >= 2010 and int(string) <= 2020:
                            fields.remove(j)
                        break
                elif i[0] == "eyr":
                        if int(string) >= 2020 and int(string) <= 2030:
                            fields.remove(j)
                        break
                elif i[0] == "hgt":
                    if string[len(string) - 2: len(string)] == "cm":
                            if int(string[0: len(string)-2]) >= 150  and int(string[0: len(string)-2]) <= 193:
                                fields.remove(j)
                    elif string[len(string) - 2: len(string)] == "in":
                            if int(string[0: len(string)-2]) >= 59  and int(string[0: len(string)-2]) <= 76:
                                fields.remove(j)
                    break
                elif i[0] == "hcl":
                        test = True
                        for char in string:
                            if char != "#" and char != "a" and char != "b" and char != "c" and char != "d" and char != "e" and char != "f" and char != "0" and char != "1" and char != "2" and char != "3" and char != "4" and char != "5" and char != "6" and char != "7" and char != "8" and char != "9":
                                test = False
                        if string[0] == "#" and len(string) == 7 and test == True:
                            fields.remove(j)
                        break
                elif i[0] == "ecl":
                    if string == "amb" or string == "blu" or string == "brn" or string == "gry" or string == "grn" or string == "hzl" or string == "oth":
                        fields.remove(j)
                    break
                elif i[0] == "pid":
                    if len(string) == 9:
                        fields.remove(j)
                    break
                else:
                    fields.remove(j)
                    break

                fields.remove(j)
        
    if fields == [] or fields == ["cid"]:
        counter += 1
print(counter)




