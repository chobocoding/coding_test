# https://www.acmicpc.net/problem/10845
# 시간 제한 0.5초 입력 최대 10000 -> O(n^2)미만으로 해결해야 함
# FIFO를 구현 해야 함
# deque를 활용하여 위의 문제를 구현하면 해결 가능

from collections import deque
import sys
queue = deque()

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    command = sys.stdin.readline().rstrip()
    if command == "pop":
        if len(queue) == 0: print(-1)
        else: print(queue.popleft())
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if len(queue) == 0: print(1)
        else: print(0)
    elif command == "front":
        if len(queue) == 0: print(-1)
        else: print(queue[0])

    elif command == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[-1])

    else:
        queue.append(command[5:])
