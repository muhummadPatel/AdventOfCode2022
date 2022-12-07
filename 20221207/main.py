class Node:
    def __init__(self, parent, name, size):
        self.parent = parent
        self.name = name
        self._size = int(size)
        self._children = []

    def get_children(self):
        return self._children

    def get_child_by_name(self, name):
        for child in self._children:
            if child.name == name:
                return child

        raise Exception(f'Child of {self.name} with name {name} not found')

    def add_child(self, node):
        self._children.append(node)

    def is_dir(self):
        return self._size == 0

    def size(self):
        tot = self._size
        for child in self._children:
            tot += child.size()

        return tot

    def print_with_level(self, level):
        indent = ''.join(['  ' for i in range(level)])
        dir_marker = '>' if self.is_dir() else ''
        str = f'{indent}-{dir_marker}{self.name} ({self.size()})\n'

        for i in range(len(self._children)):
            str += self._children[i].print_with_level(level + 1)

        return str

    def __str__(self):
        return self.print_with_level(0)


def read_input(filepath):
    with open(filepath, 'r') as f:
        return [line.strip() for line in f.readlines()]


def build_tree(lines):
    root = Node(None, '/', 0)
    current = root
    for line in lines[1:]:
        if line == '$ cd ..':
            current = current.parent
        elif line.startswith('$ cd'):
            dir_name = line.split(' ')[2]
            current = current.get_child_by_name(dir_name)
        elif line == '$ ls':
            pass
        else:
            if line.startswith('dir'):
                dir_name = line.split(' ')[1]
                new_node = Node(current, dir_name, 0)
            else:
                size, filename = line.split(' ')
                new_node = Node(current, filename, size)
            current.add_child(new_node)

    return root


def get_dir_sizes(node, dir_sizes=[]):
    if node.is_dir():
        dir_sizes.append((node.name, node.size()))
    for child in node.get_children():
        get_dir_sizes(child, dir_sizes)

    return dir_sizes


def main():
    input = read_input('input.txt')

    file_tree = build_tree(input)
    dir_sizes = get_dir_sizes(file_tree)

    # part 1
    total_dirs_size = sum(map(lambda dir: dir[1], filter(lambda dir: dir[1] <= 100_000, dir_sizes)))
    print(f'Part 1 - total size of dirs with size <= 100_000: {total_dirs_size}')

    # part 2
    total_disk_space = 70_000_000
    used_disk_space = file_tree.size()
    required_unused_disk_space = 30_000_000
    sorted_dirs = sorted(dir_sizes, key=lambda dir: dir[1])
    to_delete = None
    for dir in sorted_dirs:
        if total_disk_space - (used_disk_space - dir[1]) >= required_unused_disk_space:
            to_delete = dir
            break
    print(f'Part 2 - smallest dir we need to delete for the update: {to_delete}')


if __name__ == '__main__':
    main()
