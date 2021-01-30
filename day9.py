# https://adventofcode.com/2020/day/9


def get_input(file):
    with open(file) as f:
        return f.read().splitlines()


def find_previous_sum(sequence, index, limit):
    j = index - limit
    while j < index - 1:
        k = j + 1
        while k < index:
            if int(sequence[j]) + int(sequence[k]) == int(sequence[index]):
                return sequence[j], sequence[k]
            k += 1
        j += 1


def find_first_weak_number(sequence):
    i = limit = 25
    while i < len(sequence) and find_previous_sum(sequence, i, limit) is not None:
        i += 1
    return int(sequence[i]) if i < len(sequence) else None


def find_encryption_weakness(sequence, weak_number):
    i = 0
    while i < len(sequence) - 1:
        total = int(sequence[i])
        min_number = int(sequence[i])
        max_number = min_number
        j = i + 1
        while j < len(sequence) and total < weak_number:
            number = int(sequence[j])
            if number < min_number:
                min_number = number
            if number > max_number:
                max_number = number
            total += number
            if total == weak_number:
                return min_number + max_number
            j += 1
        i += 1


def main():
    input_sequence = get_input('data/day9-input.txt')
    weak_number = find_first_weak_number(input_sequence)
    print(f'Weak number: {weak_number}')
    encryption_weakness = find_encryption_weakness(input_sequence, weak_number)
    print(f'Encryption weakness: {encryption_weakness}')


if __name__ == '__main__':
    main()
