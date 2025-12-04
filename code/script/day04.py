#!/usr/bin/env python

import sys
sys.path.insert(0, 'code/utils/')
from grid import Grid

diagram = Grid('input/day04.txt')

def count_rolls(adjacent_positions):
    return adjacent_positions.count('@')

def find_rolls(grid, remove_immediately):
    rolls_to_remove = []
    n_removed = 0
    for x in range(grid.shape[1]): # columns
        for y in range(grid.shape[0]): # rows
            if grid.get(x, y)=='@':
                adjacent_positions = grid.get_adjacent_positions(x, y)
                if count_rolls(adjacent_positions) < 4:
                    n_removed += 1
                    if remove_immediately:
                        grid.update(x, y)
                    else:
                        rolls_to_remove.append((x, y))
    return rolls_to_remove, n_removed

def solve(diagram):
    rolls_to_remove, n_removed = find_rolls(diagram, remove_immediately=False)
    part1 = n_removed

    # Remove all rolls identified in Part 1
    for x, y in rolls_to_remove:
        diagram.update(x, y)
        
    # Start Part 2 counter at the number of rolls removed in Part 1
    part2 = part1
    
    # Then iterate through the grid again, this time removing rolls as we go
    no_more_to_remove = False
    while not no_more_to_remove:
        rolls_to_remove, removed_this_pass = find_rolls(diagram, remove_immediately=True)
        if removed_this_pass==0:
            no_more_to_remove = True
        else:
            part2 += removed_this_pass
    
    return part1, part2

part1, part2 = solve(diagram)

print(part1)
print(part2)