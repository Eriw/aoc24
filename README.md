# Advent of Code 2024 Framework

A Python framework for solving Advent of Code 2024 puzzles.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Eriw/aoc24.git
cd aoc24
```

2. Install dependencies:
```bash
python3 -m pip install -r requirements.txt
```

## Usage

### Creating a New Day's Solution

To create a new solution file for a day:
```bash
python3 cli.py new <day>
```
For example: `python3 cli.py new 1` will create:
- A solution file at `solutions/day01.py`
- A test file at `tests/test_day01.py`
- An empty input file at `inputs/day01.txt`

### Working on Solutions

1. Paste your puzzle input into the corresponding input file in `inputs/`
2. Edit the solution file in `solutions/`
3. Update the test file with example input and expected results
4. Run your solution:
```bash
python3 solutions/day01.py
```

### Running Tests

To run tests for a specific day:
```bash
python3 -m pytest tests/test_day01.py -v
```

## Features

### Input Utilities
- `read_input(day)`: Read raw input
- `read_input_lines(day)`: Read input as lines
- `read_input_integers(day)`: Read input as integers
- `read_input_grid(day)`: Read input as 2D grid
- `extract_numbers(text)`: Extract all numbers from text

### Algorithm Utilities
- `manhattan_distance(p1, p2)`: Calculate Manhattan distance
- `bfs(start, get_neighbors, is_target)`: Breadth-first search
- `dijkstra(start, get_neighbors_with_costs, is_target)`: Dijkstra's algorithm
- `get_path(came_from, start, end)`: Reconstruct path from search results

## Dependencies
- requests: For downloading input files
- numpy: For matrix operations
- networkx: For graph problems
- parse: For parsing input strings
- pytest: For running tests