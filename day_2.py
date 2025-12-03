"""My solutions for day 2 of AOC 2025"""

def get_input() -> list[str]:
    """Returns the puzzle input"""

    with open("input_day_2.txt", "r") as file:
        ranges = file.readline().split(',')
        return [(id_range.split('-')) for id_range in ranges]


def process_part_one(data: list[str]) -> int:
    """Returns the answer to part one"""

    total = 0
    for id_range in data:
        for id in range(int(id_range[0]), int(id_range[1])+1):
            s_id = str(id)
            midpoint = len(s_id) // 2
            if s_id[:midpoint] == s_id[midpoint:]:
                total += id
            
    return total

def is_repeating_pattern(s_id: str) -> bool:
    """Check if s_id is made of a pattern repeated at least twice"""

    n = len(s_id)
    for pattern_len in range(1, n // 2 + 1):
        if n % pattern_len == 0:
            pattern = s_id[:pattern_len]
            if pattern * (n // pattern_len) == s_id:
                return True
            
    return False

def process_part_two(data: list[str]) -> int:
    """Returns the answer to part two"""

    total = 0
    for id_range in data:
        for id in range(int(id_range[0]), int(id_range[1])+1):
            s_id = str(id)
            if is_repeating_pattern(s_id):
                total += id
            
    return total


if __name__ == "__main__":
    puzzle_input = get_input()
    first_part = process_part_one(puzzle_input)
    second_part = process_part_two(puzzle_input)
    print(f'First part: {first_part}')
    print(f'Second part: {second_part}')