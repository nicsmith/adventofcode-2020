
def generate_bag_trees(file):
    bag_contained_by_tree = {}
    bag_contains_tree = {}
    with open(file) as f:
        for line in f.read().splitlines():
            bag_colour, contained_by = line.split("bags contain")
            bag_colour = bag_colour.strip()
            for containing_bag in contained_by.split(','):
                bag_details = containing_bag.strip().split(' ')
                if bag_contains_tree.get(bag_colour) is None:
                    bag_contains_tree[bag_colour] = {}
                if bag_details[0] != 'no':
                    colour = f"{bag_details[1].strip()} {bag_details[2].strip()}"
                    if bag_contained_by_tree.get(colour) is None:
                        bag_contained_by_tree[colour] = []
                    bag_contained_by_tree[colour].append(bag_colour)
                    quantity = int(bag_details[0].strip())
                    bag_contains_tree[bag_colour][colour] = quantity
    return bag_contained_by_tree, bag_contains_tree


def traverse_bags(rules, colour):
    contained_by = rules.get(colour)
    if contained_by is not None:
        for c in contained_by:
            yield c
            yield from traverse_bags(rules, c)


def traverse_bags2(rules, colour):
    contains = rules.get(colour)
    total = 0
    if not contains:
        return total
    for c in contains:
        c_count = contains[c]
        total += c_count + c_count * traverse_bags2(rules, c)
    return total


def solve_part1(rules, colour):
    return len(set(traverse_bags(rules, colour)))


def main():
    contained_by, contains = generate_bag_trees('data/day7-input.txt')
    bag_count = solve_part1(contained_by, 'shiny gold')
    bag_count2 = traverse_bags2(contains, 'shiny gold')
    print(f"Part1: {bag_count} bags")
    print(f"Part2: {bag_count2} bags")


if __name__ == '__main__':
    main()
