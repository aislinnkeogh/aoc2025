#!/usr/bin/env python

with open('input/day01.txt') as f:
    instructions = [(line[0], int(line[1:])) for line in f]

def solve(instructions):
    part1 = 0
    part2 = 0
    dial = 50

    for direction, steps in instructions:
        n = 1 if direction=="R" else -1
        for i in range(steps):
            dial += n
            dial = 0 if dial > 99 else 99 if dial < 0 else dial # reset if out of bounds
            part2 += dial==0
        part1 += dial==0

    return part1, part2

part1, part2 = solve(instructions)

print(part1)
print(part2)