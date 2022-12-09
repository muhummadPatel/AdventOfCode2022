import math


def read_input(filepath):
    with open(filepath, 'r') as f:
        commands = [[cmd for cmd in line.split()] for line in f.readlines()]
        return [(cmd[0].upper(), int(cmd[1])) for cmd in commands]



def follow_head(head, tail):
    x1, y1 = head
    x2, y2 = tail
    d_x, d_y = x1 - x2, y1 - y2
    dist = int(math.sqrt(math.pow(d_x, 2) + math.pow(d_y, 2)))

    if dist > 1:  # not adjacent
        # try:
        #     x_dir = -1 if d_x > 0 else 1
        #     mv_x = int(x_dir * (d_x / d_x))
        # except ZeroDivisionError:
        #     mv_x = 0

        # try:
        #     y_dir = -1 if d_y > 0 else 1
        #     mv_y = int(y_dir * (d_y / d_y))
        # except ZeroDivisionError:
        #     mv_y = 0
        # return (tail[0] + mv_x, tail[1] + mv_y)
        if d_x > 0 and d_y > 0:  # top right
            new_tail = (x2 + 1, y2 + 1)
        elif d_x < 0 and d_y > 0:  # top left
            new_tail = (x2 - 1, y2 + 1)
        elif d_x < 0 and d_y < 0:  # bottom left
            new_tail = (x2 - 1, y2 - 1)
        elif d_x > 0 and d_y < 0:  # bottom right
            new_tail = (x2 + 1, y2 - 1)
        elif d_x < 0:  # left
            new_tail = (x2 - 1, y2)
        elif d_x > 0:  # right
            new_tail = (x2 + 1, y2)
        elif d_y > 0:  # top
            new_tail = (x2, y2 + 1)
        elif d_y < 0:  # bottom
            new_tail = (x2, y2 - 1)
        return new_tail

    return tail


def move(head, tails, command, tail_positions):
    direction, distance = command
    new_head = head
    new_tails = [t for t in tails]
    for _move in range(distance):
        if direction == 'U':
            new_head = (new_head[0], new_head[1] + 1)
        elif direction == 'D':
            new_head = (new_head[0], new_head[1] - 1)
        elif direction == 'R':
            new_head = (new_head[0] + 1, new_head[1])
        elif direction == 'L':
            new_head = (new_head[0] - 1, new_head[1])

        new_tails[0] = follow_head(new_head, new_tails[0])
        for i in range(1, len(new_tails)):
            new_tails[i] = follow_head(new_tails[i - 1], new_tails[i])

        tail_positions.add(new_tails[-1])
        # print(new_head, new_tails)
    # print('---')

    return new_head, new_tails, tail_positions


def main():
    commands = read_input('input.txt')

    # part 1
    head = (0, 0)
    tails = [(0, 0)]
    tail_positions = {tails[-1]}
    for command in commands:
        head, tails, tail_positions = move(head, tails, command, tail_positions)
    print(f'Part 1 - distinct positions covered by tail knot 1: {len(tail_positions)}')

    # part 2
    head = (0, 0)
    tails = [(0, 0) for i in range(9)]
    tail_positions = {tails[-1]}
    for command in commands:
        head, tails, tail_positions = move(head, tails, command, tail_positions)
    print(f'Part 2 - distinct positions covered by tail knot 9: {len(tail_positions)}')


if __name__ == '__main__':
    main()
