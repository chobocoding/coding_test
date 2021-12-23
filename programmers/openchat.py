def solution(record):
    id_dict = {}
    answer = []
    for i in record:
        lst = i.split(' ')
        if lst[0] in ['Enter', 'Change']:
            id_dict[lst[1]] = lst[2]

    for i in record:
        lst = i.split(' ')
        if lst[0] == 'Enter':
            answer.append(id_dict[lst[1]] +  '님이 들어왔습니다.')
        elif lst[0] == 'Leave':
            answer.append(id_dict[lst[1]] + '님이 나갔습니다.')
    return answer
