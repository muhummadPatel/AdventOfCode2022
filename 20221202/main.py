def read_strategy(filepath):
    with open(filepath, 'r') as f:
        return [
            line.strip().upper().split(' ')
            for line in f.readlines()
        ]


def score_round_1(round):
    shape_scores = {'X': 1, 'Y': 2, 'Z': 3}
    shape_score = shape_scores[round[1]]

    draws = ['AX', 'BY', 'CZ']
    wins = ['AY', 'BZ', 'CX']
    outcome = ''.join(round)
    if outcome in draws:
        outcome_score = 3
    elif outcome in wins:
        outcome_score = 6
    else:
        outcome_score = 0

    return shape_score + outcome_score


def score_round_2(round):
    shape_scores = {
        'X': {'A': 3, 'B': 1, 'C': 2},  # loss
        'Y': {'A': 1, 'B': 2, 'C': 3},  # draw
        'Z': {'A': 2, 'B': 3, 'C': 1}  # win
    }

    outcome = round[1]
    if outcome == 'X':  # loss
        outcome_score = 0
    elif outcome == 'Y':  # draw
        outcome_score = 3
    elif outcome == 'Z':  # win
        outcome_score = 6

    return shape_scores[outcome][round[0]] + outcome_score


def main():
    strategy = read_strategy('input.txt')

    scores1 = map(score_round_1, strategy)
    print(f'total score for strategy guide reading 1: {sum(scores1)}')

    scores2 = map(score_round_2, strategy)
    print(f'total score for strategy guide reading 2: {sum(scores2)}')


if __name__ == '__main__':
    main()
