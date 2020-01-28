#!/bin/python3

import math
import os
import random
import re
import sys
import itertools as it

def get_line_num(num_list, line_num = 1):
    N = len(num_list)
    if N == 1:
        return line_num
    d = num_list.pop(0)
    inc = (d - 1) * math.factorial(N-1)
    line_num = (line_num + inc) % (10**9 + 7)
    num_list = [x - 1 if x > d else x for x in num_list]
    return get_line_num(num_list, line_num)

def build_single_perm(num_list, perm_list):
    i = 0
    if num_list.count(0) != len(perm_list):
        print("List / permutation mismatch", num_list, len(perm_list))
        exit
    for el in num_list:
        if el == 0:
            num_list[i] = perm_list.pop(0)
    return num_list

def find_missing_nums(num_list):
    N = len(num_list)
    all_nums = []
    all_nums.extend(range(1, N+1))
    all_nums = [x for x in all_nums if x not in num_list]
    return all_nums

def get_perms_of_missing(num_list):
    N = len(num_list)
    missing = find_missing_nums(num_list)
    n = len(missing)
    plist = list(it.permutations(missing, n))
    print(len(plist))
    return plist

def distinct_pairs(li):
    return [(e1, e2) for e1 in li for e2 in li if(e1 < e2)]

def get_next_perm(li):
    next_perm = []
    oli = li.copy()
    pairs = distinct_pairs(list(range(0,len(li))))
    # print(pairs)
    next_perm = []
    for i, p in enumerate(pairs):
        # print(p)
        li[p[0]], li[p[1]] = li[p[1]], li[p[0]]
        if i == 0:
            next_perm = li.copy()
        if li > oli:
            if li < next_perm:
                # print(li)
                next_perm = li.copy()
        li = oli.copy()
    return next_perm
    
# Complete the solve function below.
def solve(x):
    ox = x.copy()
    N = len(x)
    line_num_sum = 0
    if N < 1:
        print("Empty List!")
        exit
    elif N > 3 * 10**5:
        print("List too long!")
        exit
    # elif N != len(set(x)):
    #     print("All values not distinct!")
    #     exit
    # elif N != max(x):
    #     print("Max value in list not length, malformed list!")
    #     exit
    else:
        plist = get_perms_of_missing(x)
        print(plist)
        for pel in plist:
            x = ox.copy()
            pel = list(pel)
            print("x: ", x)
            print("pel: ", pel)
            single_perm = build_single_perm(x, pel)
            print("perm: ", single_perm)
            line_num_sum = (line_num_sum + get_line_num(single_perm)) % (10^9 + 7) 
    return line_num_sum 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(str(result) + '\n')

    fptr.close()
