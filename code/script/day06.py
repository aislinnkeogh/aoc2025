#!/usr/bin/env python

from math import prod

def parse(filepath, part):
    
    if part==1:
        with open(filepath) as f:
            lines = [line.strip().split() for line in f]
            problems = [[int(line[i]) for line in lines[:-1]] for i in range(len(lines[0]))]
            operators = lines[-1]
            
    elif part==2:
        with open(filepath) as f:
            lines = [line.rstrip("\n") + " " for line in f]
            line_length = len(lines[0])
            block_starts = [i for i in range(line_length) if lines[-1][i] != " "] + [line_length]
            operators = lines[-1].split()
            problems = []
            for i, start in enumerate(block_starts[:-1]):
                current_block = []
                for j in range(start, block_starts[i+1]):
                    this_col = [line[j] for line in lines[:-1]]
                    if all([char==" " for char in this_col]): # stop once we're just in whitespace and move to the next block
                        problems.append(current_block)
                        break
                    else:
                        current_block.append(int("".join([char for char in this_col])))
        
    return problems, operators

def solve(problems, operators):
    answer = 0
    for i, problem in enumerate(problems):
        if operators[i] == '+':
            answer += sum(problem)
        elif operators[i] == '*':
            answer += prod(problem)
    return answer

problems1, operators1 = parse('input/day06.txt', 1)
problems2, operators2 = parse('input/day06.txt', 2)

part1 = solve(problems1, operators1)
part2 = solve(problems2, operators2)

print(part1)
print(part2)