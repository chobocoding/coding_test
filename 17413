# https://www.acmicpc.net/problem/17413


# 제한시간 1초인데 최대 입력 갯수 10만개 -> O(N^2) 미만으로 알고리즘 작성
# 태크, 단어로 문자열을 나눠야 함
# 그냥 하나 씩 옮겨가면서 문자열 추가하자!

string = input()
result = ''
index = 0
temp = ''
while True:
    if index == len(string):
        result += temp[-1: :-1]
        break
    if string[index] == '<':
        result += temp[-1: :-1]
        temp = ''
        result += string[index]
        while string[index] != '>':
            index += 1
            result += string[index]
    elif string[index].isalnum():
        temp += string[index]

    else:
        result += temp[-1: :-1] + ' '
        temp = ''
   
    index += 1
print(result)
