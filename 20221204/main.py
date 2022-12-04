def read_input(filepath):
    with open(filepath, 'r') as f:
        return [
            [list(map(lambda x: int(x), rng.split('-'))) for rng in pair.strip().split(',')]
            for pair in f.readlines()
        ]


def fully_contains(range1, range2):
    ''''Returns True if range1 fully contains range2'''
    return range1[0] <= range2[0] and range1[1] >= range2[1]


def overlaps(range1, range2):
    return (range1[1] >= range2[0] and range1[1] <= range2[1]) \
        or (range2[1] >= range1[0] and range2[1] <= range1[1])


def main():
    pairs = read_input('input.txt')

    # part 1
    fully_contained_pairs = 0
    for pair in pairs:
        if fully_contains(pair[0], pair[1]) or fully_contains(pair[1], pair[0]):
            fully_contained_pairs += 1
    print(f'part 1 - pairs which are fully contained: {fully_contained_pairs}')

    # part 2
    overlapping_pairs = 0
    for pair in pairs:
        if overlaps(pair[0], pair[1]):
            overlapping_pairs += 1
    print(f'part 2 - pairs which overlap at all: {overlapping_pairs}')


if __name__ == '__main__':
    main()
