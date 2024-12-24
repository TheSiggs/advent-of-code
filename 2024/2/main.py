
reports = []
with open("in.txt", "r") as f:
    text = f.read()
    lines = text.split("\n")
    for line in lines:
        report = line.split(' ')
        if len(report) == 1:
            break
        report = [int(i) for i in report]
        reports.append(report)

safe_count = 0
for report in reports:
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.
    report_safe = False
    for i, _ in enumerate(report):
        fixed_report = report.copy()
        fixed_report.pop(i)
        increasing = False
        decreasing = False
        safe = True
        lp = 0
        rp = 1
        print(fixed_report)
        while True:
            if rp == len(fixed_report):
                break
            l = fixed_report[lp]
            r = fixed_report[rp]
            print(l, r, l - r)
            if not safe:
                # go to next report
                break
            if abs(l - r) < 1 or abs(l - r) > 3:
                safe = False
                break
            if l < r:
                decreasing = True
            if l > r:
                increasing = True
            if increasing and decreasing:
                safe = False
                break
            lp += 1
            rp += 1
        if safe:
            report_safe = True

    print(safe, increasing, decreasing)
    if report_safe:
        safe_count += 1
    print()

print(safe_count)
