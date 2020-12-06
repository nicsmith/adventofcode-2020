
def test():
    assert get_seat_id('FBFBBFFRLR') == 357
    assert get_seat_id('FFFBBBFRRR') == 119
    assert get_seat_id('BBFFBBFRLL') == 820


def get_input(file):
    with open(file) as f:
        return f.read().splitlines()


def get_seat_id(seat_partition):
    row = int(seat_partition[0:7].replace('B', '1').replace('F', '0'), 2)
    col = int(seat_partition[7:10].replace('R', '1').replace('L', '0'), 2)
    return row * 8 + col


def find_first_empty_seat(sorted_seats):
    for i in range(len(sorted_seats) - 1):
        if sorted_seats[i + 1] - sorted_seats[i] > 1:
            return sorted_seats[i] + 1


def get_sorted_seat_list(data):
    return sorted(list(get_seat_id(line) for line in data))


def main():
    test()
    seats = get_sorted_seat_list(get_input('data/day5-input.txt'))
    print(f"Highest seat ID: {seats[-1]}")
    print(f"My seat: {find_first_empty_seat(seats)}")


if __name__ == '__main__':
    main()
