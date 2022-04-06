# https://www.acmicpc.net/problem/17298 

import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
NGE = [-1] * N
index = []
for i in range(0, N):
    while len(index) != 0 and A[index[-1]] < A[i]:
        NGE[index.pop()] = A[i]
    index.append(i)
for n in range(len(NGE)):
    print(NGE[n], end=' ')

'''
점점 큰 수를 찾으면서 왼쪽 수와 비교하면서 NGE값을 업데이트 해나감..
'''
# 코드 출처 : https://blog.naver.com/dhkimxx/222657694311
