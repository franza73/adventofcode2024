#!/usr/local/bin/python3
'''
Advent of code day 5 - 2024
'''
from itertools import combinations
from functools import cmp_to_key


def process(data_file):
    '''
    Process ordering.
    '''
    total1 = total2 = 0
    cmp_fun = {}
    paths = []
    with open(data_file, 'r', encoding="ascii") as file:
        for line in file.readlines():
            for line in line.splitlines():
                if '|' in line:
                    cmp_fun[line] = 1
                    a, b = line.split('|')
                    cmp_fun[b + '|' + a] = -1
                elif ',' in line:
                    paths += [line.split(',')]
    for path in paths:
        is_good_path = True
        for a, b in combinations(path, 2):
            if cmp_fun[a + '|' + b] == -1:
                if is_good_path:
                    is_good_path = False
        if is_good_path:
            total1 += int(path[len(path) // 2])
        else:
            path = sorted(path, key=cmp_to_key(
                          lambda a, b: cmp_fun[a + '|' + b]))
            total2 += int(path[len(path) // 2])
    return total1, total2


if __name__ == "__main__":
    FILE = 'day5.txt'
    sol1, sol2 = process(FILE)
    print('First solution:', sol1)
    assert sol1 == 5208
    print('Second solution:', sol2)
    assert sol2 == 6732
