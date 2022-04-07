# https://www.acmicpc.net/problem/9093

import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    word_list = sys.stdin.readline().rstrip().split(' ')
    for i in word_list:
        print(i[-1: :-1], end=' ')
    print()
