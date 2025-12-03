#!/usr/bin/env python

with open('input/day03.txt') as f:
    batteries = [[x for x in line.strip()] for line in f]

def max_joltage(bank, n_batteries):
    # the ith digit in the number should be the highest number in the bank which is more than n_batteries-i from the end
    digits = []
    for i in range(n_batteries):
        next_digit = max(bank[:len(bank)-(n_batteries-i)+1])
        idx = bank.index(next_digit)
        digits.append(next_digit)
        bank = bank[idx+1:]
    return int("".join(digits))

part1 = 0
for bank in batteries:
    part1 += max_joltage(bank, 2)

part2 = 0
for bank in batteries:
    part2 += max_joltage(bank, 12)

print(part1)
print(part2)