import math
slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))


def test():
    data = [
        '..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#',
        '.#...##..#.', '..#.##.....', '.#.#.#....#', '.#........#',
        '#.##...#...', '#...##....#', '.#..#...#.#']
    assert solve_part1(data) == 7
    assert solve_part2(data) == 336


def get_input(file):
    with open(file) as f:
        return f.read().splitlines()


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
    return get_tree_count(data, slopes[1])


def solve_part2(data):
    return math.prod(get_tree_count(data, s) for s in slopes)


def main():
    test()
    data = get_input('data/day3-input.txt')
    print(f'part1: {solve_part1(data)} trees')
    print(f'part2: {solve_part2(data)} is the product of encountered trees')


if __name__ == '__main__':
    main()
