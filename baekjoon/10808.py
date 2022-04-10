# https://www.acmicpc.net/problem/10808

from collections import Counter

input_string = input()
count_char = Counter(input_string)

for i in range(26):
    try:
        print(count_char[chr(97+i)], end =' ')
    except:
        print(0, end =' ')
