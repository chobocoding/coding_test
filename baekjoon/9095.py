# https://www.acmicpc.net/problem/9095

import sys

num_dict = {
    1 : 1,
    2 : 2,
    3 : 4
}
result = 0
def count_123(n):
    output = 0
    if n in num_dict:
        return num_dict[n]
    else:
        output = count_123(n-3) + count_123(n-2) + count_123(n-1)
        num_dict[n] = output
        return output

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    print(count_123(int(sys.stdin.readline().rstrip())))
