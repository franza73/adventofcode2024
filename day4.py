#!/usr/local/bin/python3
'''
Advent of code day 4 - 2024
'''
from itertools import product


DIRS = [[-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]]
XSET = set(['M', 'S'])


def process(data_file):
    '''
    Process matrix to count x-mas measures by two methods
    '''
    def _count_method_1():
        cnt = 0
        for d_x, d_y in DIRS:
            x, y = first_x + d_x, first_y + d_y
            i = 0
            while 0 <= x < len_x and 0 <= y < len_y and i < 3 and \
                    matrix[x][y] == 'MAS'[i]:
                x += d_x
                y += d_y
                i += 1
            if i == 3:
                cnt += 1
        return cnt

    def _count_method_2():
        cnt = 0
        s1 = set([matrix[first_x-1][first_y-1],
                  matrix[first_x+1][first_y+1]])
        s2 = set([matrix[first_x-1][first_y+1],
                  matrix[first_x+1][first_y-1]])
        if s1 == XSET and s2 == XSET:
            cnt += 1
        return cnt

    total1 = total2 = 0
    matrix = []
    with open(data_file, 'r', encoding="ascii") as file:
        for line in file.readlines():
            for line in line.splitlines():
                matrix += [list(line)]
    len_x, len_y = len(matrix), len(matrix[0])
    for first_x, first_y in product(range(len_x), range(len_y)):
        if matrix[first_x][first_y] == 'X':
            total1 += _count_method_1()
        if 0 < first_x < len_x - 1 and 0 < first_y < len_y - 1 and \
                matrix[first_x][first_y] == 'A':
            total2 += _count_method_2()
    return total1, total2


if __name__ == "__main__":
    FILE = 'day4.txt'
    sol1, sol2 = process(FILE)
    print('First solution:', sol1)
    assert sol1 == 2504
    print('Second solution:', sol2)
    assert sol2 == 1923
