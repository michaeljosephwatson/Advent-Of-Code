"""This is my solution to Advent of Code 2025 Day 1"""

def get_puzzle_input() -> list[str]:
    with open("input_day_1.txt", "r") as file:
        return file.read().splitlines()

def process(data: list[str]) -> int:

    password = 0
    state = 50

    for instruction in data:
        steps = int(instruction[1:])
        if instruction.startswith('L'):
            state -= steps
        else:
            state += steps

        state %= 100

        if state == 0:
            password += 1

    return password

def process_second_part(data: list[str]) -> int:
    
    password = 0
    state = 50

    for instruction in data:
        steps = int(instruction[1:])

        if instruction.startswith('L'):
            div, mod = divmod(-steps, -100)
            password += div
            if state != 0 and state + mod <= 0:
                password += 1
            state -= steps
        else:
            div, mod = divmod(steps, 100)
            password += div
            if state != 0 and state + mod >= 100:
                password += 1
            state += steps

        state %= 100
        
    return password


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()
    first_part = process(puzzle_input)
    second_part = process_second_part(puzzle_input)
    print(f'First part: {first_part}')
    print(f'Second part: {second_part}')