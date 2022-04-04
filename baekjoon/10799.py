# 

# O(N^2) 미만으로!
# 쇠파이프의 첫 시작과 끝 부분을 리스트로 담아둔다. -> 0 ~ N-1길이의 리스트를 만들고 쇠파이프가 있는 위치에 1을 넣고 이외는 0
# 레이저의 인덱스를 모아둔다.
# 쇠파이프가 있는 인덱스를 돌면서 레이저 인덱스에 해당하는 위치에 0을 넣는다.
# 쇠파이프 리스트를 돌면서 요소값이 0 > 1로 넘어갈 때 result += 1
''' 시도 1
# placement = input()
placement = '('*50000 + ')'*50000

laser = []
pipe = []
start_index, end_index = 0, 0

for i in range(len(placement)):
    print(i)
    open_bracket, close_bracket = 0, 0
    if placement[i] == '(':
        open_bracket += 1
        while (open_bracket - close_bracket) != 0:
            start_index, end_index = i, i+open_bracket+close_bracket
            if placement[end_index] == '(':
                open_bracket += 1
            else: 
                close_bracket += 1
        if (end_index - start_index) == 1:
            laser.append(start_index)
        else:
            pipe.append([start_index, end_index])
print(laser)
print(pipe)
    '''

# 너무 느림....
# 다른 직관이 필요해..
# '('를 만나면  open_bracket +=1, cut += 1, 단 다음 문자가 ')'가 아님
# '()'를 만나면 cut += open_bracket
# ')'를 만나면 open_bracket -= 1
placement = input()
open_bracket = 0
cut = 0
for i in range(len(placement)):
    if placement[i] =='(':
        if placement[i+1] != ')':
            open_bracket += 1
            cut += 1
        else:
            cut += open_bracket
    else:
        if placement[i-1] == '(': continue
        else: open_bracket -= 1
print(cut)
