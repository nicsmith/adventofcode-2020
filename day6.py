import os


def solve(file):
    group_answer_info = []
    with open(file) as f:
        group_answers = f.read().split(os.linesep + os.linesep)
        for group_answer in group_answers:
            unique_answers = set()
            all_answers = {}
            individual_answers = group_answer.rstrip().split(os.linesep)
            for answers in individual_answers:
                for answer in list(answers):
                    unique_answers.add(answer)
                    if answer in all_answers:
                        all_answers[answer] += 1
                    else:
                        all_answers[answer] = 1
            count_every = sum(all_answers[c] == len(individual_answers) for c in all_answers)
            group_answer_info.append((len(unique_answers), count_every))

    any_yes = 0
    all_yes = 0
    for a in group_answer_info:
        any_yes += a[0]
        all_yes += a[1]
    return any_yes, all_yes


def main():
    part1, part2 = solve('data/day6-input.txt')
    print(f"Part1: {part1}")
    print(f"Part2: {part2}")


if __name__ == '__main__':
    main()
