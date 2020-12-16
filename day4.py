# Solution for https://adventofcode.com/2020/day/4

import os
import re


def test():
    p1 = {'eyr': '1972', 'cid': '100', 'hcl': '#18171d', 'ecl': 'amb', 'hgt': '170', 'pid': '186cm', 'iyr': '2018', 'byr': '1926'}
    p2 = {'iyr': '2019', 'hcl': '#602927', 'eyr': '1967', 'hgt': '170cm', 'ecl': 'grn', 'pid': '012533040', 'byr': '1946'}
    p3 = {'hcl': 'dab227', 'iyr': '2012', 'ecl': 'brn', 'hgt': '182cm', 'pid': '021572410', 'eyr': '2020', 'byr': '1992', 'cid': '277'}
    p4 = {'hgt': '59cm', 'ecl': 'zzz', 'eyr': '2038', 'hcl': '74454a', 'iyr': '2023', 'pid':'3556412378', 'byr':'2007'}
    assert not validate_passport_part2(p1)
    assert not validate_passport_part2(p2)
    assert not validate_passport_part2(p3)
    assert not validate_passport_part2(p4)

    p5 = {'pid': '087499704', 'hgt': '74in', 'ecl': 'grn', 'iyr': '2012', 'eyr': '2030', 'byr': '1980', 'hcl': '#623a2f'}
    p6 = {'eyr':'2029', 'ecl':'blu', 'cid':'129', 'byr':'1989', 'iyr':'2014', 'pid':'896056539', 'hcl':'#a97842', 'hgt':'165cm'}
    p7 = {'hcl':'#888785', 'hgt':'164cm', 'byr':'2001', 'iyr':'2015', 'cid':'88','pid':'545766238', 'ecl':'hzl', 'eyr':'2022'}
    p8 = {'iyr':'2010', 'hgt':'158cm', 'hcl':'#b6652a', 'ecl':'blu', 'byr':'1944', 'eyr':'2021', 'pid':'093154719'}
    assert validate_passport_part2(p5)
    assert validate_passport_part2(p6)
    assert validate_passport_part2(p7)
    assert validate_passport_part2(p8)


def get_passports_from_file(file):
    passports = []
    with open(file) as f:
        lines = f.read().split(os.linesep + os.linesep)
        for line in lines:
            passport = {}
            for field in line.split():
                kvp = field.split(':')
                passport[kvp[0]] = kvp[1]
            passports.append(passport)
    return passports


valid_fields = {
    'hcl': '^#[0-9a-f]{6}$',
    'ecl': '^(amb|blu|brn|gry|grn|hzl|oth)$',
    'byr': '^19[2-9][0-9]|200[0-2]$',
    'iyr': '^201[0-9]|2020$',
    'eyr': '^202[0-9]|2030$',
    'hgt':  '^(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in$',
    'pid':  '^[0-9]{9}$'}


def validate_passport_part1(passport):
    return all(f in passport for f in valid_fields)


def validate_passport_part2(passport):
    return all(f in passport and re.match(valid_fields[f], passport[f]) for f in valid_fields)


def solve(fn, passports):
    return sum(fn(p) for p in passports)


def main():
    test()
    passports = get_passports_from_file('data/day4-input.txt')
    print(f"Part1: {solve(validate_passport_part1, passports)} valid passports")
    print(f"Part2: {solve(validate_passport_part2, passports)} valid passports")


if __name__ == '__main__':
    main()
