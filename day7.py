
def parse_rules(file):
    rules = {}
    with open(file) as f:
        for line in f.read().splitlines():
            bag_colour, contained_by = line.split("bags contain")
            for containing_bag in contained_by.split(','):
                bag_details = containing_bag.strip().split(' ')
                if bag_details[0] != 'no':
                    colour = f"{bag_details[1].strip()} {bag_details[2].strip()}"
                    if rules.get(colour) is None:
                        rules[colour] = []
                    rules[colour].append(bag_colour.strip())
    return rules


def test():
    rules = parse_rules('data/day7-test.txt')
    assert solve_part1(rules, 'shiny gold') == 4


def traverse_bags(rules, colour):
    contained_by = rules.get(colour)
    if contained_by is not None:
        for c in contained_by:
            yield c
            yield from traverse_bags(rules, c)


def solve_part1(rules, colour):
    bag_path = set()
    for bag in traverse_bags(rules, colour):
        bag_path.add(bag)
    return len(bag_path)


def main():
    test()
    rules = parse_rules('data/day7-input.txt')
    bag_count = solve_part1(rules, 'shiny gold')
    print(f"Part1: {bag_count} bags")


if __name__ == '__main__':
    main()
