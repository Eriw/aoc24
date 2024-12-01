from pathlib import Path
from typing import List, Iterator, Any
import re

def read_input(day: int) -> str:
    """Read the input file for the given day."""
    input_file = Path(__file__).parent.parent / "inputs" / f"day{day:02d}.txt"
    return input_file.read_text().strip()

def read_input_lines(day: int) -> List[str]:
    """Read the input file for the given day and split into lines."""
    return read_input(day).split('\n')

def read_input_integers(day: int) -> List[int]:
    """Read the input file and convert each line to an integer."""
    return [int(x) for x in read_input_lines(day)]

def read_input_grid(day: int) -> List[List[str]]:
    """Read the input file as a 2D grid of characters."""
    return [list(line) for line in read_input_lines(day)]

def extract_numbers(text: str) -> List[int]:
    """Extract all numbers from a string."""
    return [int(x) for x in re.findall(r'-?\d+', text)]

def chunks(lst: List[Any], n: int) -> Iterator[List[Any]]:
    """Split a list into chunks of size n."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n] 