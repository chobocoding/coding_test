# https://programmers.co.kr/learn/courses/30/lessons/81302#fn1

# 정확성 70.1.. 어거지로 짠 느낌이 강함
def solution(places):
    answer = [1, 1, 1, 1, 1]
    waiting = -1
    for place in places:
        waiting += 1
        for i in range(len(place)):
            p_idx = place[i].find('P')
            if p_idx == -1: continue
            
            if i == 4:
                if p_idx == 4: continue
                else:
                    if place[i][p_idx+1] == 'P':
                        answer[waiting] = 0
                        break    
                
            elif p_idx == 4:
                if place[i+1][p_idx] == 'P':
                    answer[waiting] = 0
                    break
                    
                if place[i+1][p_idx-1] == 'P':
                    if ((place[i+1][p_idx] == 'X') and (place[i][p_idx-1] == 'X')):
                        continue
                    else:
                        answer[waiting] = 0
                
                                    
            else:
                if ((place[i+1][p_idx] == 'P') or (place[i][p_idx+1] == 'P')):
                    answer[waiting] = 0
                    break
                if place[i+1][p_idx+1] == 'P':
                    if ((place[i+1][p_idx] == 'X') and (place[i][p_idx+1] == 'X')):
                        pass
                    else:
                        answer[waiting] = 0
                        break
                if p_idx != 0:
                    if place[i+1][p_idx-1] == 'P':
                        if ((place[i+1][p_idx] == 'X') and (place[i][p_idx-1] == 'X')):
                            continue
                        else:
                            answer[waiting] = 0
        
            
    return answer
