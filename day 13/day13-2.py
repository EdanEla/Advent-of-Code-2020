import math
with open("day13-input.txt", "r") as f:
        timeStamp = int(f.readline())
        IDList = f.readline().split(',')



def primeFactorTree(num):
    primeFactors = []
    while num % 2 == 0:
        num /= 2
        primeFactors.append(2)

    i = 3
    while i < math.sqrt(num):
        while num % i == 0:
            primeFactors.append(int(i))
            num /= i
        i += 2
    if num > 2:
        primeFactors.append(int(num))
    return primeFactors

def greatestCommonFactor(numbers):
    factors = primeFactorTree(numbers[0])
    solution = 1
    for factor in factors:
        remove = True
        for num in numbers:
            if num % factor != 0:
                remove = False
        if remove == True:
            solution *= factor
    return solution

def leastCommonMultiple(numbers):
    multiple = 1
    GCF = greatestCommonFactor(numbers)
    for num in numbers:
        multiple *= num
        multiple /= GCF
    return int(multiple)

numbers = []
offsets = []
offset = 0
for ID in IDList:
    if ID != "x":
        numbers.append(int(ID))
        offsets.append(offset)
    offset += 1

LCM = leastCommonMultiple(numbers)
timeStamp = 0
add = 1

for i in range(1, len(numbers)):
    solution = False
    while solution == False:
        solution = True
        for j in range(0, i + 1):
            if (timeStamp + offsets[j]) % numbers[j] != 0:
                solution = False
                break
        if solution == True:
            add = leastCommonMultiple(numbers[0:j])
            break
        else:
            timeStamp += add
print(timeStamp)
            
        



        
