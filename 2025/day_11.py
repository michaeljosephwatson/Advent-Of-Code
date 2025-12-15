"""My solution to day 11 of advent of code 2025"""

def get_puzzle_input() -> dict[str, list[str]]:
    """Returns the puzzle input"""
    
    with open('input_day_11.txt', 'r') as f:
        graph = {}
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            parts = line.split(': ')
            device = parts[0]
            outputs = parts[1].split()
            graph[device] = outputs
        return graph

def count_paths(graph: dict[str, list[str]], start: str, end: str, cache: dict) -> int:
    """Counts paths from start to end with caching"""
    
    if (start, end) in cache:
        return cache[(start, end)]
    
    if start == end:
        return 1
    
    if start not in graph:
        return 0
    
    total_paths = 0
    for neighbor in graph[start]:
        total_paths += count_paths(graph, neighbor, end, cache)
    
    cache[(start, end)] = total_paths
    return total_paths

def process_part_one(data: dict[str, list[str]]) -> int:
    """Returns my answer to part one"""
    
    cache = {}
    return count_paths(data, 'you', 'out', cache)

def process_part_two(data: dict[str, list[str]]) -> int:
    """Returns my answer to part two"""
    
    cache = {}
    
    paths_dac_first = (count_paths(data, 'svr', 'dac', cache) * 
                       count_paths(data, 'dac', 'fft', cache) * 
                       count_paths(data, 'fft', 'out', cache))
    
    paths_fft_first = (count_paths(data, 'svr', 'fft', cache) * 
                       count_paths(data, 'fft', 'dac', cache) * 
                       count_paths(data, 'dac', 'out', cache))
    
    return paths_dac_first + paths_fft_first

if __name__ == '__main__':
    puzzle_input = get_puzzle_input()
    print(f"Part one: {process_part_one(puzzle_input)}")
    print(f"Part two: {process_part_two(puzzle_input)}")
