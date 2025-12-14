"""My solution to day 10 of advent of code 2025"""
import re
from itertools import combinations
import z3
from collections import defaultdict

def get_puzzle_input() -> list[str]:
    """Returns the puzzle input"""
    
    with open('input_day_10.txt', 'r') as f:
        return [line.replace('\n', '') for line in f.readlines()]

def parse_machine(line: str):
    """Parse a machine line into target lights and buttons"""

    pattern_match = re.search(r'\[([.#]+)\]', line)
    pattern = pattern_match.group(1)
    target = [1 if c == '#' else 0 for c in pattern]
    
    buttons = []
    for button_match in re.finditer(r'\(([0-9,]+)\)', line):
        button_str = button_match.group(1)
        button = [int(x) for x in button_str.split(',')]
        buttons.append(button)
    
    return target, buttons

def solve_machine(target, buttons):
    """Find minimum button presses to achieve target configuration"""

    num_lights = len(target)
    num_buttons = len(buttons)
    
    for num_presses in range(num_buttons + 1):
        for combo in combinations(range(num_buttons), num_presses):
            state = [0] * num_lights
            for button_idx in combo:
                for light_idx in buttons[button_idx]:
                    state[light_idx] = 1 - state[light_idx]
            
            if state == target:
                return num_presses
    
    return float('inf')

def process_part_one(data: list[str]) -> int:
    """Returns my answer to part one"""

    total = 0
    for line in data:
        target, buttons = parse_machine(line)
        min_presses = solve_machine(target, buttons)
        total += min_presses
    return total

def parse_joltage(line: str):
    """Parse joltage requirements and buttons"""

    buttons = []
    for button_match in re.finditer(r'\(([0-9,]+)\)', line):
        button_str = button_match.group(1)
        button = [int(x) for x in button_str.split(',')]
        buttons.append(button)
    
    joltage_match = re.search(r'\{([0-9,]+)\}', line)
    joltage_str = joltage_match.group(1)
    target_joltage = [int(x) for x in joltage_str.split(',')]
    
    return target_joltage, buttons

def solve_joltage(target, buttons):
    """Find minimum button presses"""

    solver = z3.Optimize()
    button_presses = z3.IntVector("button_presses", len(buttons))
    
    button_indices = defaultdict(list)
    for i, btn in enumerate(buttons):
        solver.add(button_presses[i] >= 0)
        for j in btn:
            button_indices[j].append(i)
    
    for j, indices in button_indices.items():
        solver.add(target[j] == sum(button_presses[i] for i in indices))
    
    presses = z3.Sum(button_presses)
    solver.minimize(presses)
    solver.check()
    return solver.model().eval(presses).as_long()

def process_part_two(data: list[str]) -> int:
    """Returns my answer to part two"""

    total = 0
    for line in data:
        target_joltage, buttons = parse_joltage(line)
        min_presses = solve_joltage(target_joltage, buttons)
        total += min_presses
    return total


if __name__ == '__main__':
    puzzle_input = get_puzzle_input()
    print(f'Part one answer: {process_part_one(puzzle_input)}')
    print(f'Part two answer: {process_part_two(puzzle_input)}')