find = "MAS"
with open("in.txt", "r") as f:
    text = f.read()
    lines = text.split('\n')

for i, line in enumerate(lines):
    if len(line) == 0:
        lines.pop(i)


def check_adjacent(lines, x, y, text):
    # Check Up
    valid_up = True
    for i, v in enumerate(text):
        if y - i < 0:
            valid_up = False
            break
        if lines[y - i][x] != v:
            valid_up = False
            break

    # Check Down
    valid_down = True
    for i, v in enumerate(text):
        if y + i > len(lines) - 1:
            valid_down = False
            break
        if lines[y + i][x] != v:
            valid_down = False
            break

    # Check Left
    valid_left = True
    for i, v in enumerate(text):
        if x - i < 0:
            valid_left = False
            break
        if lines[y][x - i] != v:
            valid_left = False
            break

    # Check Right
    valid_right = True
    for i, v in enumerate(text):
        if x + i > len(lines[y]) - 1:
            valid_right = False
            break
        if lines[y][x + i] != v:
            valid_right = False
            break

    # Check Up Left
    valid_up_left = True
    for i, v in enumerate(text):
        if y - i < 0 or x - i < 0:
            valid_up_left = False
            break
        if lines[y - i][x - i] != v:
            valid_up_left = False
            break

    # Check Up Right
    valid_up_right = True
    for i, v in enumerate(text):
        if y - i < 0 or x + i > len(lines[y - i]) - 1:
            valid_up_right = False
            break
        if lines[y - i][x + i] != v:
            valid_up_right = False
            break

    # Check Bottom Left
    valid_bottom_left = True
    for i, v in enumerate(text):
        if y + i > len(lines) - 1 or x - i < 0:
            valid_bottom_left = False
            break
        if lines[y + i][x - i] != v:
            valid_bottom_left = False
            break

    # Check Bottom Right
    valid_bottom_right = True
    for i, v in enumerate(text):
        if y + i > len(lines) - 1 or x + i > len(lines[y + i]) - 1:
            valid_bottom_right = False
            break
        if lines[y + i][x + i] != v:
            valid_bottom_right = False
            break

    return valid_up + valid_down + valid_left + valid_right + valid_up_left + valid_up_right + valid_bottom_left + valid_bottom_right


def check_x_shape(lines, x, y, text):
    if len(text) % 2 == 0:
        raise Exception("text must have a middle point")
    middle_char = text[len(text) // 2]
    first_seg = text[:len(text) // 2]
    last_seg = text[len(text) // 2 + 1::]
    first_seg_reverse = first_seg[::-1]
    last_seg_reverse = last_seg[::-1]
    if lines[y][x] != middle_char:
        return False

    # Up Right to Bottom Left
    valid_up_right_to_bottom_left = True
    for i, v in enumerate(first_seg):
        if y - len(first_seg) + i < 0 or x - len(first_seg) + i < 0:
            valid_up_right_to_bottom_left = False
            break
        if lines[y - len(first_seg) + i][x - len(first_seg) + i] != v:
            valid_up_right_to_bottom_left = False
            break

    for i, v in enumerate(last_seg):
        if y + i + 1 >= len(lines) or x + i + 1 >= len(lines[y + i + 1]):
            valid_up_right_to_bottom_left = False
            break
        if lines[y + i + 1][x + i + 1] != v:
            valid_up_right_to_bottom_left = False
            break

    # Up Left to Bottom Right
    valid_up_left_to_bottom_right = True
    for i, v in enumerate(first_seg):
        if y - len(first_seg) + i < 0 or x + len(first_seg) - i >= len(lines[y - len(first_seg) + i]):
            valid_up_left_to_bottom_right = False
            break
        if lines[y - len(first_seg) + i][x + len(first_seg) - i] != v:
            valid_up_left_to_bottom_right = False
            break

    for i, v in enumerate(last_seg):
        if y + i + 1 >= len(lines) or x + i - 1 > len(lines[y + i + 1]):
            valid_up_left_to_bottom_right = False
            break
        if lines[y + i + 1][x + i - 1] != v:
            valid_up_left_to_bottom_right = False
            break

    # Up Right to Bottom Left Reversed
    valid_up_right_to_bottom_left_reversed = True
    for i, v in enumerate(last_seg_reverse):
        if y - len(last_seg_reverse) + i < 0 or x - len(last_seg_reverse) + i < 0:
            valid_up_right_to_bottom_left_reversed = False
            break
        if lines[y - len(last_seg_reverse) + i][x - len(last_seg_reverse) + i] != v:
            valid_up_right_to_bottom_left_reversed = False
            break

    for i, v in enumerate(first_seg_reverse):
        if y + i + 1 >= len(lines) or x + i + 1 >= len(lines[y + i + 1]):
            valid_up_right_to_bottom_left_reversed = False
            break
        if lines[y + i + 1][x + i + 1] != v:
            valid_up_right_to_bottom_left_reversed = False
            break

    # Up Left to Bottom Right Reversed
    valid_up_left_to_bottom_right_reversed = True
    for i, v in enumerate(first_seg):
        if y + len(first_seg) - i >= len(lines) or x - len(first_seg) + i < 0:
            valid_up_left_to_bottom_right_reversed = False
            break
        if lines[y + len(first_seg) - i][x - len(first_seg) + i] != v:
            valid_up_left_to_bottom_right_reversed = False
            break

    for i, v in enumerate(last_seg):
        if y + i - 1 > len(lines) or x + i + 1 >= len(lines[y + i - 1]):
            valid_up_left_to_bottom_right_reversed = False
            break
        if lines[y + i - 1][x + i + 1] != v:
            valid_up_left_to_bottom_right_reversed = False
            break

    return (
        (valid_up_right_to_bottom_left_reversed and valid_up_left_to_bottom_right_reversed) +
        (valid_up_right_to_bottom_left and valid_up_left_to_bottom_right) +
        (valid_up_right_to_bottom_left_reversed and valid_up_left_to_bottom_right) +
        (valid_up_right_to_bottom_left and valid_up_left_to_bottom_right_reversed)
    )


x = 0
y = 0
rolling = 0

for yi, yv in enumerate(lines):
    for xi, xv in enumerate(yv):
        rolling += check_x_shape(lines, xi, yi, find)

print(rolling)
