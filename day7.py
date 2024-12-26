#!/usr/local/bin/python3
'''
Advent of code day 7 - 2024
'''


def process(data_file):
    '''
    Evaluate expressions
    '''
    def _eval1(res, vals):
        ''' First evaluation method '''
        if len(vals) == 1:
            return res == vals[0]
        if res % vals[-1] == 0 and _eval1(res // vals[-1], vals[:-1]):
            return True
        if res > vals[-1] and _eval1(res - vals[-1], vals[:-1]):
            return True
        return False
    
    def _eval2(res, vals):
        ''' Second evaluation method '''
        if len(vals) == 1:
            return res == vals[0]
        if res % vals[-1] == 0 and _eval2(res // vals[-1], vals[:-1]):
            return True
        if res > vals[-1] and _eval2(res - vals[-1], vals[:-1]):
            return True
        if res > vals[-1]:
            d, m = divmod(res - vals[-1], 10**(len(str(vals[-1]))))
            if m == 0 and _eval2(d, vals[:-1]):
                return True
        return False
    
    res1 = res2 = 0
    with open(data_file, 'r', encoding="ascii") as file:
        for line in file.readlines():
            for line in line.splitlines():
                res, vals = line.split(':')
                res = int(res)
                vals = list(map(int, vals.split()))
                if _eval1(res, vals):
                    res1 += res
                if _eval2(res, vals):
                    res2 += res 
    return res1, res2


if __name__ == "__main__":
    FILE = 'day7.txt'
    sol1, sol2 = process(FILE)
    print('First solution:', sol1)
    assert sol1 == 538191549061
    print('Second solution:', sol2)
    assert sol2 == 34612812972206
