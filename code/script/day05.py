#!/usr/bin/env python

import bisect

with open('input/day05.txt') as f:
    lines = [line.strip() for line in f]

def parse(lines):
    break_point = lines.index('')
    ranges = [[int(n) for n in r.split("-")] for r in lines[:break_point]]
    ids = [int(n) for n in lines[break_point+1:]]
    return ranges, ids

def in_ranges(n, ranges, startpoints):
    i = bisect.bisect_right(startpoints, n) - 1 # bisect_right --> where would we have to insert this number to preserve the order? need to check the range at the index before this
    if i >= 0:
        return ranges[i][0] <= n <= ranges[i][1]
    return False

def solve(ranges, ids):
    ranges.sort(key=lambda r: r[0]) # sort by start so we only have to compare each range against the previous one to see if there's any overlap
    merged_ranges = [ranges[0]]
    for start, stop in ranges[1:]:
        if start > merged_ranges[-1][1] + 1: # no overlap, append this range to the list as is
            merged_ranges.append([start, stop])
        else: # overlap: set the end point of the previous range to whichever is higher out of it and the end point of the current range
            merged_ranges[-1][1] = max(merged_ranges[-1][1], stop)
    startpoints = [r[0] for r in merged_ranges]
    part1 = sum(in_ranges(ingredient, merged_ranges, startpoints) for ingredient in ids)
    part2 = sum(stop - start + 1 for start, stop in merged_ranges)
    return part1, part2

ranges, ids = parse(lines)
part1, part2 = solve(ranges, ids)

print(part1)
print(part2)