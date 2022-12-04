def read_input(filepath):
    with open(filepath, 'r') as f:
        return [
            rucksack.strip()
            for rucksack in f.readlines()
        ]


def get_common_item(lists):
    sets = [set(lst) for lst in lists]
    common_items = sets[0].intersection(*sets[1:])

    if len(common_items) > 1:
        raise Exception(f'Found multiple common items in lists: {lists}')

    return common_items.pop()


def get_priority(item):
    if item.isupper():
        offset = 38
    else:
        offset = 96

    return ord(item) - offset


def groups(rucksacks, group_size):
    for i in range(0, len(rucksacks), group_size):
        yield rucksacks[i:i + group_size]


def main():
    rucksacks = read_input('input.txt')

    # part 1
    common_items = [
        get_common_item([rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]])
        for rucksack in rucksacks
    ]
    priorities = [get_priority(item) for item in common_items]
    print(f'part 1 answer - sum of common item priorities per rucksack: {sum(priorities)}')

    # part 2
    common_items = []
    for group in groups(rucksacks, 3):
        common_items.append(get_common_item(group))
    priorities = [get_priority(item) for item in common_items]
    print(f'part 2 answer - sum of common item priorities per group of 3: {sum(priorities)}')


if __name__ == '__main__':
    main()
