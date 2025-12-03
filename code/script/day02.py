#!/usr/bin/env python

import re

with open('input/day02.txt') as f:
    ranges = [[int(n) for n in r.split("-")] for line in f for r in line.split(",")]

def solve(ranges):
    part1 = 0
    part1_pattern = re.compile(r"^(.+)\1$") # single repeat of the capturing group (.+)
    part2 = 0
    part2_pattern = re.compile(r"^(.+)\1+$") # two or more repeats of the capturing group

    for start, stop in ranges:
        for idx in range(start, stop+1):
            id_str = str(idx)
            if part1_pattern.match(id_str):
                part1 += idx
                continue
            if part2_pattern.match(id_str):
                part2 += idx

    return part1, part1+part2

part1, part2 = solve(ranges)

print(part1)
print(part2)