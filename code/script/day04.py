#!/usr/bin/env python

import sys
sys.path.insert(0, 'code/utils/')
from grid import Grid

diagram = Grid('input/day04.txt')

def count_rolls(adjacent_positions):
    return adjacent_positions.count('@')

part1 = 0
rolls_to_remove = []
for x in range(diagram.shape[1]): # columns
    for y in range(diagram.shape[0]): # rows
        if diagram.get(x, y)=='@':
            adjacent_positions = diagram.get_adjacent_positions(x, y)
            if count_rolls(adjacent_positions) < 4:
                part1 += 1
                rolls_to_remove.append((x, y))

# Remove all rolls identified in Part 1
for x, y in rolls_to_remove:
    diagram.update(x, y)

# Start Part 2 counter at the number of rolls removed in Part 1
part2 = part1

# Then iterate through the grid again, this time removing rolls as we go
no_more_to_remove = False
while not no_more_to_remove:
    removed_this_pass = 0
    for x in range(diagram.shape[1]):
        for y in range(diagram.shape[0]):
            if diagram.get(x, y)=='@':
                adjacent_positions = diagram.get_adjacent_positions(x, y)
                if count_rolls(adjacent_positions) < 4:
                    diagram.update(x, y)
                    part2 += 1
                    removed_this_pass += 1
    if removed_this_pass==0:
        no_more_to_remove = True

print(part1)
print(part2)