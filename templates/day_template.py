import sys
from pathlib import Path

# Add parent directory to Python path for imports
sys.path.append(str(Path(__file__).parent.parent))

from utils.input import read_input_lines

def parse_input(lines):
    """Parse the input data into appropriate data structure."""
    # Example:
    # return [[int(x) for x in line.split()] for line in lines]
    return lines

def solve_part1(data):
    """
    Solve part 1 of the puzzle.
    
    Args:
        data: Parsed input data
    
    Returns:
        Solution to part 1
    """
    pass

def solve_part2(data):
    """
    Solve part 2 of the puzzle.
    
    Args:
        data: Parsed input data
    
    Returns:
        Solution to part 2
    """
    return 0  # Update when part 2 is available

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