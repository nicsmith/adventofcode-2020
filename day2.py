def test():
    passwords = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    assert validate_part1(passwords[0])
    assert not validate_part1(passwords[1])
    assert validate_part1(passwords[2])
    assert validate_part2(passwords[0])
    assert not validate_part2(passwords[1])
    assert not validate_part2(passwords[2])


def extract_password_data(password_data):
    policy, password = password_data.split(':')
    policy = policy.strip().split(' ')
    indexes = policy[0].split("-")
    return int(indexes[0]), int(indexes[1]), policy[1], password.strip()


def validate_part1(password_entry):
    min_count, max_count, character, password = extract_password_data(password_entry)
    char_count = password.count(character)
    return not (char_count < min_count or char_count > max_count)


def validate_part2(password_entry):
    i, j, character, password = extract_password_data(password_entry)
    return (password[i - 1] == character) ^ (password[j - 1] == character)


def solve(passwords, function):
    return sum(function(p) for p in passwords)


def get_input(file):
    with open(file) as f:
        return f.read().splitlines()


def main():
    test()
    data = get_input('data/day2-input.txt')
    print(f"Part 1 : {solve(data, validate_part1)}")
    print(f"Part 2 : {solve(data, validate_part2)}")


if __name__ == '__main__':
    main()
