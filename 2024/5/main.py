# Setup
with open('in.txt', 'r') as f:
    text = f.read()

text_arr = text.split('\n')[:-1]
spliti = 0
for i, v in enumerate(text_arr):
    if v == '':
        spliti = i

rules = text_arr[:spliti]
rules = [v.split('|') for v in rules]
rulesDict = {}

reports = text_arr[spliti + 1:]
reports = [v.split(',') for v in reports]

for i, o in rules:
    if i not in rulesDict:
        rulesDict[i] = set()
    rulesDict[i].add(o)

# Part 1
rolling = 0
for report in reports:
    valid = True
    for i, reportA in enumerate(report):
        if not valid:
            break
        for reportB in report[i + 1:]:
            if reportB in rulesDict and reportA in rulesDict[reportB]:
                valid = False
                break
    if valid:
        middle_val = report[len(report) // 2]
        rolling += int(middle_val)
print(rolling)


# Part 2
def fix_report(report):
    valid = False
    while not valid:
        thisValid = True
        for ia, reportA in enumerate(report):
            if not thisValid:
                break
            for ib, reportB in enumerate(report[ia + 1:]):
                if reportB in rulesDict and reportA in rulesDict[reportB]:
                    idxb = ia + 1 + ib
                    report[ia] = reportB
                    report[idxb] = reportA
                    thisValid = False
                    break
        if thisValid:
            valid = True
    return int(report[len(report) // 2])


rolling = 0
for report in reports:
    valid = True
    fixed_middle = 0
    for i, reportA in enumerate(report):
        if not valid:
            break
        for reportB in report[i + 1:]:
            if reportB in rulesDict and reportA in rulesDict[reportB]:
                valid = False
                fixed_middle = fix_report(report)
                break
    if not valid:
        rolling += fixed_middle


print(rolling)
