#!/usr/local/bin/python3
'''
Advent of code day 3 - 2024
'''
import re


def process(data_file):
    '''
    Process the program min mul, do, don't commands
    '''
    total = 0
    discounted_total = 0
    enabled = True
    with open(data_file, 'r', encoding="ascii") as file:
        for line in file.readlines():
            for line in line.splitlines():
                regex = r'(do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))'
                for cmd, a, b in re.findall(regex, line):
                    if cmd == 'do()':
                        enabled = True
                    elif cmd == 'don\'t()':
                        enabled = False
                    else:
                        prod = int(a) * int(b)
                        total += prod
                        if enabled:
                            discounted_total += prod
    return total, discounted_total


if __name__ == "__main__":
    FILE = 'day3.txt'
    sol1, sol2 = process(FILE)
    print('First solution:', sol1)
    assert sol1 == 173785482
    print('Second solution:', sol2)
    assert sol2 == 83158140
