import math
slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))


def test():
    data = [
        '..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#',
        '.#...##..#.', '..#.##.....', '.#.#.#....#', '.#........#',
        '#.##...#...', '#...##....#', '.#..#...#.#']
    m = generate_map(data)
    assert solve_part1(m) == 7
    assert solve_part2(m) == 336


def get_input(file):
    with open(file) as f:
        return f.read().splitlines()


def generate_map(data):
    a_map = []
    for line in data:
        a_map.append(list(line))
    return a_map


def get_tree_count(a_map, slope):
    row = 0
    column = 0
    tree_count = 0
    x_delta = slope[0]
    y_delta = slope[1]
    while row < len(a_map) - y_delta:
        row += y_delta
        column = (column + x_delta) % len(a_map[row])
        if a_map[row][column] == '#':
            tree_count += 1
    return tree_count


def solve_part1(data):
    return get_tree_count(generate_map(data), slopes[1])


def solve_part2(data):
    return math.prod(get_tree_count(generate_map(data), s) for s in slopes)


def main():
    test()
    data = get_input('data/day3-input.txt')
    print(f'part1: {solve_part1(data)} trees')
    print(f'part2: {solve_part2(data)} is the product of encountered trees')


if __name__ == '__main__':
    main()
