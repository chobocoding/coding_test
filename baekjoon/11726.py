# https://www.acmicpc.net/problem/11726

import sys

num_dict = {
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 5
}

def count(n):
    if n in num_dict:
        return num_dict[n]
    else:
        output = count(n-2) + count(n-1)
        num_dict[n] = output
        return output % 10007
print(count(int(sys.stdin.readline().rstrip())))
