#!/usr/local/bin/python3
'''
Advent of code day 2 - 2024
'''


def is_valid(s):
    '''
    Is valid sequence?
    '''
    if s[0] == s[1]:
        return False
    if s[0] < s[1]:
        for i in range(1, len(s)):
            if not 1 <= s[i] - s[i-1] <= 3:
                return False
    else:
        for i in range(1, len(s)):
            if not -3 <= s[i] - s[i-1] <= -1:
                return False
    return True


def can_fix(s):
    '''
    Can the fix the sequence by removing one item?
    '''
    for v in range(len(s)):
        if is_valid(s[:v] + s[v+1:]):
            return True
    return False


def process(data_file):
    '''
    Process the data and calculates the number of valid sequences for two
    different criteria.
    '''
    n_safe = 0
    n_safe_fix = 0
    with open(data_file, 'r', encoding="ascii") as file:
        for line in file.readlines():
            s = list(map(int, line.split()))
            if is_valid(s):
                n_safe += 1
            elif can_fix(s):
                n_safe_fix += 1
    return n_safe, n_safe + n_safe_fix


if __name__ == "__main__":
    FILE = 'day2.txt'
    sol1, sol2 = process(FILE)
    print('First solution:', sol1)
    assert sol1 == 463
    print('Second solution:', sol2)
    assert sol2 == 514
