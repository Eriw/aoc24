import argparse
import os
import shutil
from pathlib import Path

def create_day(day: int):
    """Create a new day's solution files from template."""
    template_path = Path(__file__).parent / "templates" / "day_template.py"
    solution_path = Path(__file__).parent / "solutions" / f"day{day:02d}.py"
    
    if not template_path.exists():
        print(f"Template file not found at {template_path}")
        return
    
    if solution_path.exists():
        print(f"Solution file already exists for day {day}")
        return
    
    shutil.copy(template_path, solution_path)
    print(f"Created solution file for day {day}")

    # Create test file
    test_template_path = Path(__file__).parent / "templates" / "test_template.py"
    test_path = Path(__file__).parent / "tests" / f"test_day{day:02d}.py"
    
    if test_template_path.exists():
        # Read template and format with day number
        test_content = test_template_path.read_text()
        test_content = test_content.format(day=day)
        test_path.write_text(test_content)
        print(f"Created test file for day {day}")
    else:
        print(f"Test template file not found at {test_template_path}")

    # Create input directory if it doesn't exist
    input_dir = Path(__file__).parent / "inputs"
    input_dir.mkdir(exist_ok=True)
    
    # Create empty input file
    input_file = input_dir / f"day{day:02d}.txt"
    input_file.touch()
    print(f"Created input file at {input_file}")

def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2024 CLI")
    parser.add_argument("command", choices=["new"], help="Command to execute")
    parser.add_argument("day", type=int, help="Day number (1-25)")
    
    args = parser.parse_args()
    
    if args.command == "new":
        if not 1 <= args.day <= 25:
            print("Day must be between 1 and 25")
            return
        create_day(args.day)

if __name__ == "__main__":
    main() 