from solutions.day01 import parse_input, solve_part1, solve_part2

EXAMPLE_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""

def test_part1_example():
    data = parse_input(EXAMPLE_INPUT.splitlines())
    assert solve_part1(data) == 11

def test_part2_example():
    data = parse_input(EXAMPLE_INPUT.splitlines())
    assert solve_part2(data) == 31

def test_parse_input():
    data = parse_input(EXAMPLE_INPUT.splitlines())
    assert len(data) == 2  # Two lists
    assert data[0] == [3, 4, 2, 1, 3, 3]  # Left list
    assert data[1] == [4, 3, 5, 3, 9, 3]  # Right list
