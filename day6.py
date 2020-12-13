# Solution for https://adventofcode.com/2020/day/6

import os


def solve(file):
    sum_unique_answers = 0
    sum_common_answers = 0
    with open(file) as f:
        lines = f.read().split(os.linesep + os.linesep)
        for line in lines:
            line = line.rstrip().split(os.linesep)
            answers = list(map(set, line))
            sum_unique_answers += len(set.union(*answers))
            sum_common_answers += len(set.intersection(*answers))
    return sum_unique_answers, sum_common_answers


def main():
    unique_answers, common_answers = solve('data/day6-input.txt')
    print(f"Part1, sum of unique answers: {unique_answers}")
    print(f"Part2, sum of common answers: {common_answers}")


if __name__ == '__main__':
    main()
