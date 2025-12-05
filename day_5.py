"""My solution to Day 5 of Advent of Code 2025."""

from math import inf

def get_puzzle_input() -> list[str]:
    with open('input_day_5.txt', 'r') as f:
        return [line.replace('\n', '') for line in f.readlines()]
        # 177 for \n

def process_part_one(data: list[str]) -> int:
    """Returns my answer for part one"""

    separation_index = 177
    ranges = data[:separation_index]
    ingreedients = data[separation_index+1:]

    fresh_ingreedients = 0
    for ingreedient in ingreedients:
        for ran in ranges:
            lower, upper = ran.split('-')
            if int(ingreedient) >= int(lower) and int(ingreedient) <= int(upper):
                fresh_ingreedients += 1
                break

    return fresh_ingreedients  

def process_part_two(data: list[str]) -> int:
    """Returns my answer for part two"""

    separation_index = 177
    ranges = data[:separation_index]
    
    parsed_ranges = []
    for ran in ranges:
        lower, upper = ran.split('-')
        parsed_ranges.append((int(lower), int(upper)))
    
    parsed_ranges.sort()
    
    merged = []
    for lower, upper in parsed_ranges:
        if merged and lower <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], upper))
            continue
    
        merged.append((lower, upper))
    
    total = 0
    for lower, upper in merged:
        total += upper - lower + 1
    
    return total

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()
    print(f'First part: {process_part_one(puzzle_input)}')  
    print(f'Second part: {process_part_two(puzzle_input)}') 