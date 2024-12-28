import re

with open("in.txt", "r") as f:
    text = f.read()
    instructions = re.findall(r"don't\(\)|do\(\)|mul\(\b[0-9]{1,3}\b,\b[0-9]{1,3}\b\)", text)

rolling = 0
do = True
for instruction in instructions:
    print(instruction)
    if instruction == "don't()":
        do = False
        continue
    if instruction == "do()":
        do = True
        continue
    if do:
        nums = re.findall(r"\b[0-9]{1,3}\b", instruction)
        rolling += int(nums[0]) * int(nums[1])

print(rolling)
