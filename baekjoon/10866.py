# https://www.acmicpc.net/problem/10866

# deque 모듈을 이용하여 구현하면 될듯
from collections import deque
import sys
queue = deque()

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    command = sys.stdin.readline().rstrip()
    if 'push_front' in command:
        queue.appendleft(command[11:])
    elif 'push_back' in command:
        queue.append(command[11:])
    elif 'pop_front' in command:
        if len(queue) == 0: print(-1)
        else: print(queue.popleft())
    elif 'pop_back' in command:
        if len(queue) == 0: print(-1)
        else: print(queue.pop())
    elif 'size' in command:
        print(len(queue))
    elif 'empty' in command:
        if len(queue) == 0: print(1)
        else: print(-1)
    elif 'front' in command:
        if len(queue) == 0: print(-1)
        else: print(queue[0])
    else:
        if len(queue) == 0: print(-1)
        else: print(queue[-1])
