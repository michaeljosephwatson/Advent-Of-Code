"""This is my solution to day 3 of Advent of Code 2025."""

def get_puzzle_input() -> list[str]:
    """Returns the puzzle input"""

    with open('input_day_3.txt', 'r') as f:
        data = list(map(lambda s: s.replace('\n', ''), f.readlines()))
        return data 
    
def process_part_one(data: list[str]) -> int:
    """Returns the answer to part one of the problem"""

    joltage = 0
    for bank in data:
        powers = list(map(lambda x: int(x), list(bank)))
        max_power = max(powers[:-1])
        max_power_index = bank.find(str(max_power))

        remaining_powers = list(map(lambda x: int(x), list(bank[max_power_index+1:])))
        second_max_power = max(remaining_powers)
        combined_joltage = str(max_power) + str(second_max_power)

        joltage += int(combined_joltage)

    return joltage

def process_part_two(data: list[str]) -> int:
    """Returns the answer to part two of the problem"""

    n = 12
    joltage = 0
    for bank in data:
        combined_joltage = ''
        for i in range(n):
            range_index = -(n-1-i)
            if range_index != 0:
                powers = list(map(lambda x: int(x), list(bank[:range_index])))
            else:
                powers = list(map(lambda x: int(x), list(bank)))

            max_power = max(powers)
            max_power_index = bank.find(str(max_power))
            combined_joltage += str(max_power)
            bank = bank[max_power_index+1:]

        joltage += int(combined_joltage)

    return joltage



if __name__ == "__main__":
    puzzle_input = get_puzzle_input()
    print(f'First part: {process_part_one(puzzle_input)}')
    print(f'Second part: {process_part_two(puzzle_input)}')
    
