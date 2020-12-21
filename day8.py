# https://adventofcode.com/2020/day/8
# Part 2 solved by brute-force :(
# TODO: revisit part 2 using a graph with instructions as node and operand as weight


def split_operation(op):
    op_split = op.split(' ')
    return op_split[0], int(op_split[1])


def get_instructions(file):
    with open(file) as f:
        instructions = f.read().splitlines()
        return instructions


def run_code(instructions):
    accumulator = 0
    visited_instructions = set()
    i = 0
    while i < len(instructions) and i not in visited_instructions:
        operation, operand = split_operation(instructions[i])
        if operation == 'acc':
            accumulator += operand
        elif operation == 'jmp':
            i += operand - 1
        visited_instructions.add(i)
        i += 1
    return i == len(instructions), accumulator


def swap_op(op, operand):
    if op == 'nop' and int(operand) != 0:
        return 'jmp'
    elif op == 'jmp':
        return 'nop'
    else:
        return op


def fix_code(instructions):
    finished = False
    accumulator = 0
    i = 0
    while i < len(instructions) and not finished:
        operation, operand = split_operation(instructions[i])
        original_instruction = instructions[i]
        if operation in ('nop', 'jmp'):
            operation = swap_op(operation, operand)
            instructions[i] = f'{operation} {operand}'
            finished, accumulator = run_code(instructions)
            instructions[i] = original_instruction
        i += 1
    return accumulator


def main():
    instructions = get_instructions('data/day8-input.txt')
    print(run_code(instructions)[1])
    print(fix_code(instructions))


if __name__ == '__main__':
    main()
