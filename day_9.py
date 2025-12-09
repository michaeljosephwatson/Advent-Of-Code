"""My solution to day 9 of advent of code 2025"""

from itertools import combinations, pairwise

def get_puzzle_input() -> list[tuple[int, int]]:
    """Returns the puzzle input"""

    with open('input_day_9.txt', 'r') as f:
        return [tuple(int(num) for num in line.replace('\n', '').split(',')) for line in f.readlines()]
    
def process_part_one(data: list[tuple[int, int]]) -> int:
    """Returns my answer to part one"""

    max_area = 0
    for (x1, y1), (x2, y2) in combinations(data, 2):
        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        area = width * height
        
        if area > max_area:
            max_area = area
    
    return max_area

def process_part_two(data: list[tuple[int, int]]) -> int:
    """Returns my answer to part two"""

    # Build perimeters
    perimeter = set()
    for (x1, y1), (x2, y2) in pairwise(data + [data[0]]):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                perimeter.add((x, y))
    
    # Sort rectangle
    rectangles = []
    for (x1, y1), (x2, y2) in combinations(data, 2):
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        rectangles.append(((x1, y1), (x2, y2), area))
    rectangles.sort(key=lambda x: x[2], reverse=True)
    
    # Find rectangle with no perimeter points
    for (x1, y1), (x2, y2), area in rectangles:
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)
        
        valid = True
        for (px, py) in perimeter:
            if min_x < px < max_x and min_y < py < max_y:
                valid = False
                break
            
        if valid:
            return area
    return 0

if __name__ == '__main__':
    puzzle_input = get_puzzle_input()
    print(puzzle_input)
    print(f"Part one: {process_part_one(puzzle_input)}")
    print(f"Part two: {process_part_two(puzzle_input)}")