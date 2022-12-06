def read_input(filepath):
    with open(filepath, 'r') as f:
        return [ch for ch in f.read().strip()]


def is_uniq_seq(seq):
    return len(seq) == len(set(seq))


def find_uniq_seq(stream, length):
    for i in range(len(stream)):
        if is_uniq_seq(stream[i:i + length]):
            return i + length

    return -1


def find_packet_start_pos(stream):
    return find_uniq_seq(stream, 4)


def find_message_start_pos(stream):
    return find_uniq_seq(stream, 14)


def main():
    stream = read_input('input.txt')

    # part 1
    packet_start_pos = find_packet_start_pos(stream)
    print(f'Part 1 - start of packet at pos {packet_start_pos} in stream')

    # part 2
    message_start_pos = find_message_start_pos(stream)
    print(f'Part 1 - start of message at pos {message_start_pos} in stream')


if __name__ == '__main__':
    main()
