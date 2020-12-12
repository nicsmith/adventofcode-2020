import os
import re


def test():
    assert validate_birth_year("2002")
    assert not validate_birth_year("2003")
    assert validate_height("60in")
    assert validate_height("190cm")
    assert not validate_height("190in")
    assert not validate_height("190")
    assert validate_hair_colour("#123abc")
    assert not validate_hair_colour("#123abz")
    assert not validate_hair_colour("123abc")
    assert validate_eye_colour("brn")
    assert not validate_eye_colour("wat")
    assert validate_passport_id("000000001")
    assert not validate_passport_id("0123456789")

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
            line = line.rstrip().replace(os.linesep, ' ')
            passport = {}
            for field in line.split(' '):
                kvp = field.split(':')
                passport[kvp[0]] = kvp[1]
            passports.append(passport)
    return passports


def validate_year_between(year, year_min, year_max):
    return bool(re.match(r"^[0-9]{4}$", year)) and year_min <= int(year) <= year_max


def validate_hair_colour(hcl):
    return bool(re.match(r"#[0-9a-f]{6}", hcl))


def validate_height(height):
    p = re.compile('^([0-9]+)(cm|in)$')
    m = p.match(height)
    valid_height = False
    if bool(m):
        amount = int(m.group(1))
        unit = m.group(2)
        if unit == 'cm':
            valid_height = 150 <= amount <= 193
        elif unit == 'in':
            valid_height = 59 <= amount <= 76
    return valid_height


def validate_birth_year(year):
    return validate_year_between(year, 1920, 2002)


def validate_issue_year(year):
    return validate_year_between(year, 2010, 2020)


def validate_expiration_year(year):
    return validate_year_between(year, 2020, 2030)


def validate_eye_colour(ecl):
    return bool(re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", ecl))


def validate_passport_id(pid):
    return bool(re.match(r"^[0-9]{9}$", pid))


def validate_passport_part1(passport):
    required_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    return all(f in passport for f in required_fields)


def validate_passport_part2(passport):
    return (validate_passport_part1(passport) and
            validate_birth_year(passport['byr']) and
            validate_issue_year(passport['iyr']) and
            validate_expiration_year(passport['eyr']) and
            validate_height(passport['hgt']) and
            validate_hair_colour(passport['hcl']) and
            validate_eye_colour(passport['ecl']) and
            validate_passport_id(passport['pid']))


def solve(fn, passports):
    return sum(fn(p) for p in passports)


def main():
    test()
    passports = get_passports_from_file('data/day4-input.txt')
    print(f"Part1: {solve(validate_passport_part1, passports)} valid passports")
    print(f"Part2: {solve(validate_passport_part2, passports)} valid passports")


if __name__ == '__main__':
    main()
