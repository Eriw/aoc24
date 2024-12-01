import sys
from pathlib import Path

# Add parent directory to Python path for imports
sys.path.append(str(Path(__file__).parent.parent))

from utils.input import read_input_lines
from collections import Counter

def parse_input(lines):
    """Parse the input data into two lists of numbers."""
    left_list = []
    right_list = []
    
    for line in lines:
        # Split on whitespace and convert to integers
        left, right = [int(x) for x in line.split()]
        left_list.append(left)
        right_list.append(right)
    
    return left_list, right_list

def solve_part1(data):
    """
    Calculate total distance between sorted pairs of numbers from both lists.
    """
    left_list, right_list = data
    
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculate total distance
    total_distance = 0
    for left, right in zip(left_sorted, right_sorted):
        distance = abs(left - right)
        total_distance += distance
    
    return total_distance

def solve_part2(data):
    """
    Calculate similarity score by multiplying each number in the left list
    by the number of times it appears in the right list.
    """
    left_list, right_list = data
    
    # Count occurrences in right list
    right_counts = Counter(right_list)
    
    # Calculate similarity score
    similarity_score = 0
    for num in left_list:
        # Multiply number by its count in right list (0 if not present)
        similarity_score += num * right_counts.get(num, 0)
    
    return similarity_score

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