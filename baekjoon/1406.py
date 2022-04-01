# https://www.acmicpc.net/problem/1406

# 초기에 커서는 문장 맨 뒤 - > cursor = len(string)
# L : 커서를 왼쪽으로 한 칸 이동, 단 커서 값 0이면 무시
# D : 커서를 오른쪽으로 한 칸 이동, 단 커서 값이 len(string) 이면 무시
# B : 커서 왼쪽에 있는 문자 삭제 + (cursor -= 1). 단 커서 값이 0이면 무시 
# P $ : 커서 왼쪽에 문자 추가 + (cursor += 1)

# 시간 제한 0.3초 최대 nlogn으로 끝내야 함
# 시도 1
# 명령어 하나 씩 if 문으로 검사

# 시간 복잡도가 N^2이라 시간 초과
import sys

string = list(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
cursor = len(string)

for i in range(N):
    len_string = len(string)
    command = sys.stdin.readline().rstrip()
    if command[0] == 'L':
        if cursor == 0: continue
        else: cursor -= 1
    elif command == 'D':
        if cursor == len_string: continue
        else: cursor += 1
    elif command == 'B':
        if cursor == 0: continue
        else:
            cursor -= 1
            string.pop(cursor)
    else:
        string.insert(cursor, command[-1])
        cursor += 1
print(''.join(string))


# 시도 2
# 조건문을 cursor에 초점을 맞춤
string = list(input())
N = int(input())
cursor = len(string)

for i in range(N):
    len_string = len(string)
    command = input()
    if command[0] == 'P':
        string.insert(cursor, command[-1])
        cursor += 1
        continue

    if (cursor != 0) or (cursor != len_string) :
        if command[0] == 'L':
            cursor -= 1

        elif command == 'D':
            cursor += 1

        else: # command == 'B':
            cursor -= 1
            string.pop(cursor)

    elif cursor == len_string:
        if command[0] == 'L':
            cursor -= 1

        else: # command[0] == 'B':
            cursor -= 1
            string.pop(cursor)

    elif cursor == 0:
        if command == 'D':
            cursor += 1    
            
print(''.join(string))

#시도 3
# 특정한 경우 insert -> append, pop(index) -> pop()로 바꿔서 시간 복잡도를 줄임
string = list(input())
N = int(input())
cursor = len(string)

for i in range(N):
    len_string = len(string)
    command = input()
        
    if cursor == len_string:
        if command[0] == 'P':
            string.append(command[-1])
            cursor += 1

        elif command == 'L':
            cursor -= 1

        elif command[0] == 'B':
            cursor -= 1
            string.pop()

    elif cursor == 0:
        if command == 'D':
            cursor += 1
        elif command[0] == 'P':
            string.insert(cursor, command[-1])
            cursor += 1

    else:
        if command == 'L':
            cursor -= 1

        elif command == 'D':
            cursor += 1

        elif command == 'B':
            cursor -= 1
            string.pop(cursor)
        else:
            string.insert(cursor, command[-1])
            cursor += 1
            
print(''.join(string))

# 포기... -> 커서를 기준으로 pop, append 시간 복잡도 O(N)을 쓰지 말아야 함...ㅠ ex) insert, pop(index)
from sys import stdin
stk1 = list(stdin.readline().strip())
stk2 = []
n = int(input())
for line in stdin:
    if line[0] == 'L':
        if stk1: stk2.append(stk1.pop())
        else: continue
    elif line[0] == 'D':
            if stk2: stk1.append(stk2.pop())
            else: continue
    elif line[0] == 'B':
        if stk1: stk1.pop() 
        else: continue
    elif line[0] == 'P':
        stk1.append(line[2])
print(''.join(stk1 + list(reversed(stk2))))
