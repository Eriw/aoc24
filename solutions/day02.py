from utils.input import read_input, read_input_lines, read_input_integers, extract_numbers
from utils.algorithms import manhattan_distance, bfs, dijkstra

def parse_input(lines):
    """Parse the input data."""
    return lines

def solve_part1(data):
    """Solve part 1 of the puzzle."""
    pass

def solve_part2(data):
    """Solve part 2 of the puzzle."""
    pass

def main():
    # Get the day number from the filename
    day = int(__file__.split('day')[-1][:2])
    
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