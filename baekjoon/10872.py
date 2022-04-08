# https://www.acmicpc.net/problem/10872

import sys
N = int(sys.stdin.readline().rstrip())
facto = 1
if (N == 0) or (N == 1):
    print(facto)
else:
    for i in range(1, N+1):
        facto = facto * i
    print(facto)
