from solutions.day02 import parse_input, solve_part1, solve_part2, is_safe, is_safe_with_dampener

EXAMPLE_INPUT = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

def test_part1_example():
    data = parse_input(EXAMPLE_INPUT.splitlines())
    assert solve_part1(data) == 2  # 2 reports are safe

def test_part2_example():
    data = parse_input(EXAMPLE_INPUT.splitlines())
    assert solve_part2(data) == 4  # 4 reports are safe with Problem Dampener

def test_parse_input():
    data = parse_input(EXAMPLE_INPUT.splitlines())
    assert len(data) == 6  # 6 reports
    assert data[0] == [7, 6, 4, 2, 1]  # First report
    assert data[-1] == [1, 3, 6, 7, 9]  # Last report

def test_individual_reports():
    data = parse_input(EXAMPLE_INPUT.splitlines())
    # Test each example case mentioned in the problem
    assert is_safe(data[0]) == True   # 7 6 4 2 1: Safe (decreasing by 1 or 2)
    assert is_safe(data[1]) == False  # 1 2 7 8 9: Unsafe (2->7 increases by 5)
    assert is_safe(data[2]) == False  # 9 7 6 2 1: Unsafe (6->2 decreases by 4)
    assert is_safe(data[3]) == False  # 1 3 2 4 5: Unsafe (changes direction)
    assert is_safe(data[4]) == False  # 8 6 4 4 1: Unsafe (4->4 no change)
    assert is_safe(data[5]) == True   # 1 3 6 7 9: Safe (increasing by 1-3)

def test_individual_reports_with_dampener():
    data = parse_input(EXAMPLE_INPUT.splitlines())
    # Test each example case with Problem Dampener
    assert is_safe_with_dampener(data[0]) == True   # Safe without removing any level
    assert is_safe_with_dampener(data[1]) == False  # Unsafe regardless of removal
    assert is_safe_with_dampener(data[2]) == False  # Unsafe regardless of removal
    assert is_safe_with_dampener(data[3]) == True   # Safe by removing second level (3)
    assert is_safe_with_dampener(data[4]) == True   # Safe by removing third level (4)
    assert is_safe_with_dampener(data[5]) == True   # Safe without removing any level