# import sys
from itertools import combinations
import copy
# sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    num = list(map(str, input()))
    num_list = [num]
    lst = list(combinations(range(len(num)), 2))
    for (a, b) in lst:
        temp = copy.deepcopy(num)
        temp[a], temp[b] = temp[b], temp[a]
        if temp[0] == '0': continue
        else: num_list.append(temp)

    print(f'#{test_case}', ''.join(min(num_list)), ''.join(max(num_list)))