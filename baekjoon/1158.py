# https://www.acmicpc.net/problem/1158

# if len >=K 일 경우 count += arr[idx: idx+K] 해주고 이후 연산 ( 1씩 더하면서 찾음 )
# else: count = K%len(arr) 이후 연산
# 이를 이용하여 코딩!
N, K = map(int, input().split(' '))
iteration = 0
arr = [0] + [1]*N
idx = K
arr[K] = 0
result = [idx]
for _ in range(N-1):
    count = 0
    length = sum(arr)
    if length >= K:
        if (idx+K) > N:
            count = sum(arr[idx:]) + sum(arr[:idx+K-N+1])
            idx = idx+K-N
        else:
            count = sum(arr[idx:idx+K+1])
            idx = idx+K
    else:
        count = K - (K % length)

    while count != K:
        if idx == N:
            idx = 1
            count += arr[idx]
        else:
            idx += 1
            count += arr[idx]

    if arr[idx] == 0:
        try:
            idx = idx - arr[idx::-1].index(1)
        except:
            idx = N - arr[-1::-1].index(1)
        arr[idx] = 0
        result.append(idx)
    else:
        result.append(idx)
        arr[idx] = 0
print(f'<{result[0]}', end='')
for i in range(1, N):
    print(',', result[i], end='')
print('>')

'''
깔끔한 풀이...
N,K = map(int,input().split())
arr = [i for i in range(1,N+1)]    # 맨 처음에 원에 앉아있는 사람들

answer = []   # 제거된 사람들을 넣을 배열
num = 0  # 제거될 사람의 인덱스 번호

for t in range(N):
    num += K-1  
    if num >= len(arr):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
        num = num%len(arr)
 
    answer.append(str(arr.pop(num)))
print("<",", ".join(answer)[:],">", sep='')

'''
