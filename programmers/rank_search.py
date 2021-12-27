# https://programmers.co.kr/learn/courses/30/lessons/72412

# 시간 초과 > 3중 for문
def solution(info, query):
    conditions = []
    informations = []
    answer = []
    
    for i in range(len(query)):
        query[i] = query[i].replace('and ', '')
        query[i] = query[i].replace('- ', '')
        conditions.append(query[i].split(' '))
        
    for i in range(len(info)):
        informations.append(info[i].split(' '))
  
    for cond in conditions:
        length = len(info)
        not_sat = []
        for i in cond:
            for j in range(len(informations)):
                if j in set(not_sat): continue
                
                if i.isdigit():
                    if int(i) <= int(informations[j][-1]): continue
                    else: 
                        not_sat.append(j)
                        
                else:
                    if i in informations[j]: continue
                    else: not_sat.append(j)
        answer.append(length - len(set(not_sat)))
                         
    return answer
  
  # 시간 초과 2중 for문
  def solution(info, query):
    conditions = []
    informations = []
    answer = 0
    result = []
    for i in range(len(query)):
        query[i] = query[i].replace('and ', '')
        query[i] = query[i].replace('- ', '')
        conditions.append(query[i].split(' '))
        
    for i in range(len(info)):
        informations.append(info[i].split(' '))  

    for i in conditions:
        answer = 0
        for j in informations:
            if int(i[-1]) <= int(j[-1]):
                if len(set(i[:-1]) - set(j[:-1])) <= 0:
                    answer += 1
        result.append(answer)
    return result
  

# 풀이
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = {}
    
    for i in range(len(info)):
        infol = info[i].split(' ')
        mykey = infol[:-1]
        myval = infol[-1]
        
        for j in range(5):
            for c in combinations(mykey, j):
                tmp = ''.join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(myval))
                else:
                    info_dict[tmp] = [int(myval)]
                
    for k in info_dict:
        info_dict[k].sort()
    
    for qu in query:
        my_que = qu.split(' ')
        qu_key = my_que[:-1]
        qu_val = my_que[-1]
        
        while 'and' in qu_key:
            qu_key.remove('and')
        while '-' in qu_key:
            qu_key.remove('-')
        qu_key = ''.join(qu_key)
    
        if qu_key in info_dict:
            scores = info_dict[qu_key]
        
            if scores:
                enter = bisect_left(scores, int(qu_val))
                answer.append(len(scores) - enter)
        else:
            answer.append(0)
    
    return answer
        
