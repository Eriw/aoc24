from solutions.day02 import parse_input, solve_part1, solve_part2

EXAMPLE_INPUT = '''
# Add example input from problem description here
'''

def test_part1_example():
    data = parse_input(EXAMPLE_INPUT.strip().splitlines())
    assert solve_part1(data) == 0  # Update with expected answer

def test_part2_example():
    data = parse_input(EXAMPLE_INPUT.strip().splitlines())
    assert solve_part2(data) == 0  # Update with expected answer

def test_parse_input():
    data = parse_input(EXAMPLE_INPUT.strip().splitlines())
    assert data is not None  # Add specific assertions about parsed data structure