#!/usr/bin/env python

with open('input/day05.txt') as f:
    lines = [line.strip() for line in f]
break_point = lines.index('')
ranges = [[int(n) for n in r.split("-")] for r in lines[:break_point]]
ids = [int(n) for n in lines[break_point+1:]]

def solve(ranges, ids):
    ranges.sort(key=lambda r: r[0]) # sort by start so we only have to compare each range against the previous one to see if there's any overlap
    merged_ranges = [ranges[0]]
    for start, stop in ranges[1:]:
        if start > merged_ranges[-1][1] + 1: # no overlap, append this range to the list as is
            merged_ranges.append([start, stop])
        else: # overlap: set the end point of the previous range to whichever is higher out of it and the end point of the current range
            merged_ranges[-1][1] = max(merged_ranges[-1][1], stop)
    part1 = sum(ingredient >= start and ingredient <= stop for ingredient in ids for start, stop in merged_ranges)
    part2 = sum(stop - start + 1 for start, stop in merged_ranges)
    return part1, part2

part1, part2 = solve(ranges, ids)

print(part1)
print(part2)