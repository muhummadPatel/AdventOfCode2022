from functools import reduce


def get_elf_calories():
    with open('input.txt', 'r') as file:
        def cleanup(elf):
            return [int(x) for x in filter(lambda i: i != '', elf.split('\n'))]

        elves = [cleanup(elf) for elf in file.read().split('\n\n')]
        return [reduce(lambda i, acc: i + acc, elf) for elf in elves]


def main():
    calories = get_elf_calories()
    top3 = list(reversed(sorted(calories)))[0:3]
    print(top3)
    print('==========')
    print(sum(top3))


if __name__ == '__main__':
    main()
