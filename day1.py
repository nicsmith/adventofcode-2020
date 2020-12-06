SUM = 2020


def part1(report):
    report_len = len(report)
    for i in range(report_len - 1):
        for j in range(i + 1, report_len):
            num_1 = report[i]
            num_2 = report[j]
            if num_1 + num_2 == SUM:
                return num_1 * num_2


def part2(report):
    report_len = len(report)
    for i in range(report_len - 2):
        for j in range(i + 1, report_len):
            for k in range(j + 1, report_len):
                num_1 = report[i]
                num_2 = report[j]
                num_3 = report[k]
                if num_1 + num_2 + num_3 == SUM:
                    return num_1 * num_2 * num_3

def get_input(file):
    with open(file) as f:
        return [int(a) for a in f.read().splitlines()]


report = get_input('data/day1-input.txt')
print(part1(report))
print(part2(report))