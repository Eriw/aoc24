import sys
from pathlib import Path

# Add parent directory to Python path for imports
sys.path.append(str(Path(__file__).parent.parent))

from utils.input import read_input_lines

def parse_input(lines):
    """Parse the input data into a list of level lists."""
    return [[int(x) for x in line.split()] for line in lines]

def is_safe(levels):
    """
    Check if a report is safe according to the rules:
    1. Levels must be all increasing or all decreasing
    2. Adjacent levels must differ by 1-3
    """
    if len(levels) < 2:
        return True
    
    # Check first difference to determine if we should be increasing or decreasing
    diff = levels[1] - levels[0]
    if diff == 0:  # No change is not allowed
        return False
    
    increasing = diff > 0
    prev = levels[0]
    
    for curr in levels[1:]:
        diff = curr - prev
        # Check if direction changes or difference is too large/small
        if increasing:
            if diff <= 0 or diff > 3:
                return False
        else:
            if diff >= 0 or diff < -3:
                return False
        prev = curr
    
    return True

def is_safe_with_dampener(levels):
    """
    Check if a report is safe with the Problem Dampener.
    A report is safe if either:
    1. It's already safe without removing any level
    2. Removing one level makes it safe
    """
    # First check if it's safe without removing any level
    if is_safe(levels):
        return True
    
    # Try removing each level one at a time
    for i in range(len(levels)):
        # Create a new list without the current level
        dampened_levels = levels[:i] + levels[i+1:]
        if is_safe(dampened_levels):
            return True
    
    return False

def solve_part1(data):
    """Count how many reports are safe."""
    return sum(1 for levels in data if is_safe(levels))

def solve_part2(data):
    """Count how many reports are safe with the Problem Dampener."""
    return sum(1 for levels in data if is_safe_with_dampener(levels))

def main():
    # Get the day number from the filename
    day = int(Path(__file__).stem.split('day')[-1])
    
    # Read and parse input
    lines = read_input_lines(day)
    data = parse_input(lines)
    
    # Solve parts
    part1_solution = solve_part1(data)
    print(f"Part 1: {part1_solution}")
    
    part2_solution = solve_part2(data)
    if part2_solution is not None:
        print(f"Part 2: {part2_solution}")

if __name__ == "__main__":
    main() 