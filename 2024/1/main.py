from collections import Counter

numsL = []
numsR = []
with open("in.txt", "r") as f:
    ftext = f.read()
    lines = ftext.split("\n")
    for line in lines:
        lineS = line.split("   ")
        if len(lineS) < 2:
            continue
        numsL.append(lineS[0])
        numsR.append(lineS[1])

# Part 1
numL = sorted(numsL)
numR = sorted(numsR)
rolling = 0
for i, _ in enumerate(numL):
    num1 = int(numL[i])
    num2 = int(numR[i])
    diff = abs(num1 - num2)
    rolling += diff


counter = Counter(numsL)
for i in counter:
    counter[i] = 0

for _, v in enumerate(numsR):
    if v in counter:
        counter[v] += 1

print(counter)
rolling = 0
for i in counter:
    rolling += (int(counter[i]) * int(i))
print(rolling)
