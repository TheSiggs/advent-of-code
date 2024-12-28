from collections import Counter, defaultdict
import time
import os

simulate = False

with open('in.txt', 'r') as f:
    text = f.read()
    map = text.split('\n')
    map = [list(i) for i in map[:-1]]

# Character pos (y, x)
char = {
    '^': (-1, 0),
    '>': (0, 1),
    '<': (0, -1),
    'V': (1, 0)
}


def print_map():
    for i in map:
        print("".join(i))


def turn_90(x):
    match x:
        case '^':
            return '>'
        case '>':
            return 'V'
        case 'V':
            return '<'
        case '<':
            return '^'


def is_oob(map, y, x):
    if y < 0:
        return True, True
    if y > len(map) - 1:
        return True, True
    if x < 0:
        return True, True
    if x > len(map[y]) - 1:
        return True, True
    if map[y][x] == "#":
        return True, False
    return False, False


def detect_cycle(movements):
    visited = defaultdict(list)  # Store all visits to each coordinate

    # Track movements
    for step, coord in enumerate(movements):
        if coord in visited:
            # Check previous visits for cycles
            for start in visited[coord]:
                cycle_path = movements[start:step]  # Extract potential cycle
                cycle_length = len(cycle_path)

                # Validate cycle: Ensure it repeats at least twice
                if cycle_length > 0 and movements[start:start + cycle_length] == movements[step:step + cycle_length]:
                    return True, cycle_path
        visited[coord].append(step)

    return False, []


def infinite_loop():
    cycle, arr = detect_cycle(movements)
    return cycle


counter = Counter()
movements = []
charY, charX = 0, 0
for y, yv in enumerate(map):
    for x, xv in enumerate(yv):
        for i in char.keys():
            counter[(y, x)] = 0
        if xv in char:
            charY, charX = (y, x)

while True:
    if simulate:
        os.system('clear')
        print_map()
    charDir = map[charY][charX]
    counter[(charY, charX)] += 1
    # move char
    dirDiff = char[charDir]
    newY, newX = (charY + dirDiff[0], charX + dirDiff[1])
    obs, offMap = is_oob(map, newY, newX)
    if offMap:
        break
    if obs:
        while True:
            charDir = turn_90(charDir)
            dirDiff = char[charDir]
            newY, newX = (charY + dirDiff[0], charX + dirDiff[1])
            if map[newY][newX] != "#":
                break
    map[charY][charX] = '.'
    map[newY][newX] = charDir
    charY, charX = newY, newX
    movements.append((newY, newX))
    if infinite_loop():
        break
    if simulate:
        time.sleep(0.1)

total_positive_elements = [value for value in counter.values() if value > 0]
print(len(total_positive_elements))
