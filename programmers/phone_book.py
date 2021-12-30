# https://programmers.co.kr/learn/courses/30/lessons/42577

# 효율성 테스트 4번 시간초과...
def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    len_dict = {len(phone_book[0]) : 0}
    
    for i in range(0, len(phone_book)):
            len_dict[len(phone_book[i])] = i

    for i in range(len(phone_book)):       
        for j in range(len_dict[len(phone_book[i])], len(phone_book)):
            if phone_book[i] == phone_book[j]: continue
            if phone_book[i] == phone_book[j][:len(phone_book[i])]: return False
    return True
  
  # 다른 테스트의 시간을 많이 줄였지만 여전히 효율성 4번 시간초과
  def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    phone_dict = {}
    len_list = sorted(list(set(map(len, phone_book))))

    for i in len_list[:-1]:
        for number in phone_book:
            if len(number) < i: continue
                
            if i not in phone_dict.keys():
                phone_dict[i] = [number[:i]]
            else:
                phone_dict[i].append(number[:i])

    for i in phone_book:
        if len(i) not in phone_dict.keys(): return True
        if phone_dict[len(i)].count(i) > 1: return False
    
    return True
  
  # 해결 >> 중복값 삭제
  def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    phone_dict = {}
    len_list = sorted(list(set(map(len, phone_book))))

    for i in len_list[:-1]:
        for number in phone_book:
            if len(number) <= i: continue
                
            if i not in phone_dict.keys():
                phone_dict[i] = [number[:i]]
            else:
                phone_dict[i].append(number[:i])             
        phone_dict[i] = set(phone_dict[i]) # >>> 이 부분

    for i in phone_book:
        if len(i) not in phone_dict.keys(): return True
        if i in phone_dict[len(i)]: return False
    
    return True

# startswith함수로 간단하게 해결
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
