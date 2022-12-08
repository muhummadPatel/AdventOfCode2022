def read_input(filepath):
    with open(filepath, 'r') as f:
        return [[int(tree) for tree in line.strip()] for line in f.readlines()]


def is_visible(forest, row, col):
    tree = forest[row][col]

    from_left = True
    for c in range(0, col):
        if forest[row][c] >= tree:
            from_left = False

    from_right = True
    for c in range(col + 1, len(forest[row])):
        if forest[row][c] >= tree:
            from_right = False

    from_top = True
    for r in range(0, row):
        if forest[r][col] >= tree:
            from_top = False

    from_bottom = True
    for r in range(row + 1, len(forest)):
        if forest[r][col] >= tree:
            from_bottom = False

    return from_left or from_right or from_top or from_bottom


def get_scenic_score(forest, row, col):
    tree = forest[row][col]

    visible_to_left = 0
    for c in range(col - 1, -1, -1):
        if forest[row][c] >= tree:
            visible_to_left += 1
            break
        visible_to_left += 1

    visible_to_right = 0
    for c in range(col + 1, len(forest[row])):
        if forest[row][c] >= tree:
            visible_to_right += 1
            break
        visible_to_right += 1

    visible_to_top = 0
    for r in range(row - 1, -1, -1):
        if forest[r][col] >= tree:
            visible_to_top += 1
            break
        visible_to_top += 1

    visible_to_bottom = 0
    for r in range(row + 1, len(forest)):
        if forest[r][col] >= tree:
            visible_to_bottom += 1
            break
        visible_to_bottom += 1

    return visible_to_left * visible_to_right * visible_to_top * visible_to_bottom


def main():
    forest = read_input('input.txt')
    print(forest)

    # part 1
    visible_count = (len(forest) * 2) + (len(forest[0]) * 2) - 4  # 4 corners would be counted twice
    for row in range(1, len(forest) - 1):
        for col in range(1, len(forest[row]) - 1):
            if is_visible(forest, row, col):
                visible_count += 1
    print(f'Part 1 - count of visible trees in forest: {visible_count}')

    # part 2
    max_scenic_score = 0
    for row in range(1, len(forest) - 1):
        for col in range(1, len(forest[row]) - 1):
            scenic_score = get_scenic_score(forest, row, col)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    print(f'Part 2 - max scenic score in forest: {max_scenic_score}')


if __name__ == '__main__':
    main()
