"""My solution to day 12 of advent of code 2025"""
import sys
sys.setrecursionlimit(20000)

def get_puzzle_input() -> tuple:
    """Returns the puzzle input"""
    
    with open('input_day_12.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    
    shapes = {}
    regions = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if ':' in line and line.split(':')[0].isdigit():
            shape_id = int(line.split(':')[0])
            shape_lines = []
            i += 1
            while i < len(lines) and lines[i] and 'x' not in lines[i] and ':' not in lines[i]:
                shape_lines.append(lines[i])
                i += 1
            shapes[shape_id] = shape_lines
        elif 'x' in line:
            parts = line.split(': ')
            dims = parts[0].split('x')
            width, height = int(dims[0]), int(dims[1])
            counts = list(map(int, parts[1].split()))
            regions.append((width, height, counts))
            i += 1
        else:
            i += 1
    
    return shapes, regions


def get_variations(shapes: dict) -> dict:
    """Generate bitmask shape variations"""

    variations = {}
    
    for sid, shape in shapes.items():
        max_w = max(len(row) for row in shape)
        matrix = [[1 if c < len(row) and row[c] == '#' else 0 for c in range(max_w)] for row in shape]
        
        seen, vars = set(), []
        current = matrix
        
        for _ in range(2):
            for _ in range(4):
                min_r, max_r, min_c, max_c = len(current), -1, len(current[0]), -1
                
                for r in range(len(current)):
                    for c in range(len(current[0])):
                        if current[r][c]:
                            min_r, max_r = min(min_r, r), max(max_r, r)
                            min_c, max_c = min(min_c, c), max(max_c, c)
                
                if max_r >= 0:
                    trimmed_h = max_r - min_r + 1
                    trimmed_w = max_c - min_c + 1
                    int_rows = []
                    
                    for r in range(min_r, max_r + 1):
                        r_val = 0
                        for c in range(min_c, max_c + 1):
                            r_val = (r_val << 1) | current[r][c]
                        int_rows.append(r_val)
                    
                    sig = tuple(int_rows)
                    if sig not in seen:
                        seen.add(sig)
                        vars.append((trimmed_h, trimmed_w, int_rows))
                
                h, w = len(current), len(current[0])
                current = [[current[h - 1 - r][c] for r in range(h)] for c in range(w)]
            
            current = current[::-1]
        
        vars.sort(key=lambda x: -x[0])
        variations[sid] = vars
    
    return variations


def backtrack(grid: list[int], items: list[tuple], idx: int, w: int, h: int, variations: dict) -> bool:
    """Recursively place items backtracking"""

    if idx == len(items):
        return True
    
    sid, prev_r, prev_c = items[idx]
    start_r = prev_r if idx > 0 and items[idx - 1][0] == sid else 0
    start_c = prev_c if idx > 0 and items[idx - 1][0] == sid else 0
    
    for hv, wv, rows in variations[sid]:
        for r in range(start_r, h - hv + 1):
            c_start = start_c if r == start_r else 0
            for c in range(c_start, w - wv + 1):
                shift = w - c - wv
                
                if all(not (grid[r + i] & (rows[i] << shift)) for i in range(hv)):
                    for i in range(hv):
                        grid[r + i] |= rows[i] << shift
                    
                    items[idx] = (sid, r, c)
                    if backtrack(grid, items, idx + 1, w, h, variations):
                        return True
                    
                    for i in range(hv):
                        grid[r + i] ^= rows[i] << shift
    
    items[idx] = (sid, prev_r, prev_c)
    return False


def process_part_one(data: tuple) -> int:
    """Returns my answer to part one"""
    
    shapes, regions = data
    variations = get_variations(shapes)
    areas = {sid: sum(bin(r).count('1') for r in variations[sid][0][2]) for sid in shapes}
    
    count = 0
    for w, h, counts in regions:
        items = [(sid, 0, 0) for sid, cnt in enumerate(counts) for _ in range(cnt)]
        items.sort(key=lambda x: (-areas[x[0]], x[0]))
        
        if sum(areas[sid] for sid, _, _ in items) <= w * h:
            grid = [0] * h
            if backtrack(grid, items, 0, w, h, variations):
                count += 1
    
    return count

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()
    print(f'Part one: {process_part_one(puzzle_input)}')
