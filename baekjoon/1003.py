# https://www.acmicpc.net/problem/1003

import sys
dictionary = {
    1 : [0, 1],
    0 : [1, 0]
}

def fibo(n):
    global count_0
    global count_1
    if n in dictionary:
        count_0 = count_0 + dictionary[n][0]
        count_1 = count_1 + dictionary[n][1]
        return None

    else:
        fibo(n-1)
        fibo(n-2)
        dictionary[n] = [count_0, count_1]
        return None

N = int(sys.stdin.readline().rstrip())
for i in range(N):
    count_0 = 0
    count_1 = 0
    fibo(int(sys.stdin.readline().rstrip()))
    print(count_0, count_1)
