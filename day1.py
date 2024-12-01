#!/usr/local/bin/python3
'''
Advent of code day 1 - 2024
'''
from collections import Counter


def process(data_file):
    '''
    Read pairs of numbers from input with and calculates
    a. the sum of the absolute difference
    between these pairs of numbers after sorted.
    b. the similarity score.
    '''
    total = 0
    similarity_score = 0
    left = []
    right = []
    right_counter = Counter()
    with open(data_file, 'r', encoding="ascii") as file:
        for line in file.readlines():
            item_left, item_right = map(int, line.split())
            left.append(item_left)
            right.append(item_right)
            right_counter[item_right] += 1
    left.sort()
    right.sort()
    for item_left, item_right in zip(left, right):
        total += abs(item_left - item_right)
        similarity_score += item_left * right_counter[item_left]
    return total, similarity_score


if __name__ == "__main__":
    FILE = 'day1.txt'
    sol1, sol2 = process(FILE)
    print('First solution:', sol1)
    print('Second solution:', sol2)
