# https://www.acmicpc.net/problem/17298 

import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
NGE = [-1] * N
index = []
for i in range(0, N):
    while len(index) != 0 and A[index[-1]] < A[i]:
        NGE[index.pop()] = A[i]
    index.append(i)
for n in range(len(NGE)):
    print(NGE[n], end=' ')
