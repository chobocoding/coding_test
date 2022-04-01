# https://www.acmicpc.net/problem/1874

# 제한 시간 2초
# 최대 입력 10만
# -> 시간복잡도 nlogn가 넘지 않도록 해야함!

# 수열을 만드는 것이 불가능한 경우 NO만 출력해야하기 때문에 출력할 결과들을 따로 모아야 함(result)
# 제시된 수가 리스트 안에 없거나 리스트 안에 있는 수보다 큰 경우 -> push
# 제시된 수가 리스트 맨 위에 있을 경우 -> pop
# 제시된 수가 리스트 맨 위의 수보다 작을 경우 -> return NO
# 제시된 수를 다 처리했다면 -> result를 하나 씩 출력 후 프로그램 종료

# 코드로 구현하다보니 N번 iteration이 아닌 num_list에 값이 남아있지 않을 때 까지 동작해야 함을 깨달음

# 같아질 때 까지 1씩 증가시키니 시간이 너무 오래걸림 -> 값의 차만큼 바로 계산

# 출력을 조금 더 빠르게 개선

# (num_list[0] not in stack) 이 부분을 연산하는데 시간을 많이 잡아먹음...

N = int(input()) # 수열 길이
num_list = [] # 제시된 수열
input_num = list(range(1, N+1)) # stack으로 들어갈 수들 (오름차순)
stack = [] # 스택
result = [] # 결과 값을 저장할 list
impos = False # 출력 가능 여부

''' 첫 
# for i in range(N):
#    num_list.append(int(input()))
import time
st = time.time()
# worst case
num_list = list(range(100000, 0, -1))

while num_list:
    print(len(num_list))
    if (num_list[0] not in stack) or (num_list[0] > stack[-1]):
        stack.append(input_num.pop(0)) # insert의 시간 복잡도 N!
        result.append('+')
    
    elif num_list[0] == stack[-1]:
        result.append('-')
        stack.pop(-1)
        num_list.pop(0)

    elif num_list[0] < stack[-1]:
        print('NO')
        impos = True
        break

for i in result:
    if impos == False:
        print(i)
    else:
        pass
et = time.time()

print(et - st) # 266 sec
'''

''' 두 번째 시도


N = int(input()) # 수열 길이
num_list = [] # 제시된 수열
input_num = list(range(1, N+2)) # stack으로 들어갈 수들 (오름차순)
stack = [] # 스택
result = [] # 결과 값을 저장할 list
impos = False # 출력 가능 여부

# for i in range(N):
#    num_list.append(int(input()))
import time
st = time.time()
# worst case
num_list = list(range(100000, 0, -1))

while num_list:
    if (num_list[0] not in stack) or (num_list[0] > input_num[0]):
        diff =  num_list[0] - input_num[0]
        stack = stack + input_num[:diff+1]
        del input_num[:diff+1]
        result = result + ['+'] * diff

    elif num_list[0] == stack[-1]:
        result.append('-')
        stack.pop(-1)
        num_list.pop(0)

    elif num_list[0] < stack[-1]:
        print('NO')
        impos = True
        break

for i in result:
    if impos == False:
        print(i)
    else:
        pass
et = time.time()

print(et - st) # 118 sec
...

# 결국 혼자 푸는거 실패..
import sys

N = int(sys.stdin.readline().rstrip()) # 수열 길이
num_list = [] # 제시된 수열
input_num = 1
stack = [] # 스택
result = [] # 결과 값을 저장할 list
impos = False # 출력 가능 여부

for i in range(N):
    num_list.append(int(sys.stdin.readline().rstrip()))

while num_list:
    if num_list[0] >= input_num:
        stack.append(input_num) # insert의 시간 복잡도 N!
        result.append('+')
        input_num += 1
    
    elif num_list[0] == stack[-1]:
        result.append('-')
        stack.pop(-1)
        num_list.pop(0)

    else:
        print('NO')
        impos = True
        break

for i in result:
    if impos == False:
        sys.stdout.write(str(i)+'\n')
    else:
        pass
