# https://www.acmicpc.net/problem/2309

from itertools import combinations
nanjangs = []
for i in range(9):
    nanjangs.append(int(input()))
nanjangs.sort()
comb = combinations(nanjangs, 7)
for i in list(comb):
    if sum(i) == 100:
        for j in i:
            print(j)
        break
