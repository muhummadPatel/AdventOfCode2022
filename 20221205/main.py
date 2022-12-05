def read_input(filepath):
    with open(filepath, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]

        sep_index = lines.index('')
        stacks_input = lines[:sep_index]
        moves_input = lines[sep_index + 1:]

        return stacks_input, moves_input


def build_stacks(stacks_input):
    num_stacks = int(stacks_input[-1][-1])
    stacks = [[] for i in range(num_stacks)]

    for row in stacks_input[:-1]:
        for crate_idx in range(0, len(row), 4):
            crate = row[crate_idx:crate_idx + 3].strip()
            if crate != '':
                stacks[crate_idx // 4].insert(0, crate[1:2])

    return stacks


def apply_move_crane_9000(stacks, move):
    x = move.split(' ')
    _, num_crates, _, src, _, dest = x
    for i in range(int(num_crates)):
        stacks[int(dest) - 1].append(stacks[int(src) - 1].pop())

    return stacks


def apply_move_crane_9001(stacks, move):
    x = move.split(' ')
    _, num_crates, _, src, _, dest = x
    to_move = []
    for i in range(int(num_crates)):
        to_move.insert(0, stacks[int(src) - 1].pop())
    stacks[int(dest) - 1] += to_move

    return stacks


def main():
    stacks_input, moves_input = read_input('input.txt')

    # part 1
    stacks = build_stacks(stacks_input)
    for move in moves_input:
        stacks = apply_move_crane_9000(stacks, move)
    top_of_stacks = ''.join([stack.pop() for stack in stacks])
    print(f'part 1 - top of stacks after applying moves for crane 9000: {top_of_stacks}')

    # part 2
    stacks = build_stacks(stacks_input)
    for move in moves_input:
        stacks = apply_move_crane_9001(stacks, move)
    top_of_stacks = ''.join([stack.pop() for stack in stacks])
    print(f'part 2 - top of stacks after applying moves for crane 9001: {top_of_stacks}')


if __name__ == '__main__':
    main()
