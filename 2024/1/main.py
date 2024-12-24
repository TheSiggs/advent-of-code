
numL = []
numR = []
with open("in.txt", "r") as f:
    ftext = f.read()
    lines = ftext.split("\n")
    for line in lines:
        lineS = line.split("   ")
        if len(lineS) < 2:
            continue
        numL.append(lineS[0])
        numR.append(lineS[1])

numL = sorted(numL)
numR = sorted(numR)

rolling = 0
for i, _ in enumerate(numL):
    num1 = int(numL[i])
    num2 = int(numR[i])
    diff = abs(num1 - num2)
    print(num1, num2, diff)
    rolling += diff

print(rolling)
