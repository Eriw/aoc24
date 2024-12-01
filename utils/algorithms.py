from typing import List, Tuple, TypeVar, Callable, Dict, Set
from collections import deque
import heapq

T = TypeVar('T')

def manhattan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    """Calculate Manhattan distance between two points."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def bfs(start: T, 
        get_neighbors: Callable[[T], List[T]], 
        is_target: Callable[[T], bool]) -> Tuple[bool, Dict[T, T]]:
    """
    Breadth-first search.
    Returns (found_target, came_from) where came_from contains the path.
    """
    frontier = deque([start])
    came_from = {start: None}
    
    while frontier:
        current = frontier.popleft()
        
        if is_target(current):
            return True, came_from
            
        for next_pos in get_neighbors(current):
            if next_pos not in came_from:
                frontier.append(next_pos)
                came_from[next_pos] = current
                
    return False, came_from

def dijkstra(start: T,
             get_neighbors_with_costs: Callable[[T], List[Tuple[T, int]]],
             is_target: Callable[[T], bool]) -> Tuple[bool, Dict[T, int], Dict[T, T]]:
    """
    Dijkstra's algorithm for finding shortest path.
    Returns (found_target, costs, came_from).
    """
    frontier = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    
    while frontier:
        current_cost, current = heapq.heappop(frontier)
        
        if is_target(current):
            return True, cost_so_far, came_from
            
        for next_pos, cost in get_neighbors_with_costs(current):
            new_cost = cost_so_far[current] + cost
            
            if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                cost_so_far[next_pos] = new_cost
                came_from[next_pos] = current
                heapq.heappush(frontier, (new_cost, next_pos))
                
    return False, cost_so_far, came_from

def get_path(came_from: Dict[T, T], start: T, end: T) -> List[T]:
    """Reconstruct path from came_from dict returned by search algorithms."""
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = came_from[current]
        
    return list(reversed(path)) 