# https://www.acmicpc.net/problem/1935

def operate(operand1, operand2, operator):
    if operator == '+': return operand1 + operand2
    elif operator == '-': return operand1 - operand2
    elif operator == '*': return operand1 * operand2
    else: return operand1 / operand2

import sys

N = int(sys.stdin.readline().rstrip())
notation = sys.stdin.readline().rstrip()
temp = []
operand = {}
cal = []

for i in range(N):
    operand[chr(65+i)] = int(sys.stdin.readline().rstrip())

for i in notation:
    if i.isalpha():
        cal.append(operand[i])

idx = -1
for i in range(len(notation)):
    if notation[i].isalpha():
        idx += 1
    else:
        temp = operate(cal[idx-1], cal[idx], notation[i])
        del cal[idx-1:idx+1]
        cal.insert(idx-1, temp)
        idx -= 1

print('%.2f'%float(cal[0]))
