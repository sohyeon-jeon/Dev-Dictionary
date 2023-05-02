'''
https://school.programmers.co.kr/learn/courses/30/lessons/84512
'''
from itertools import product

# 중복순열 이용
class Test2:
    def solution(word):
        words = []
        for i in range(1,6):
            for c in product(['A','E','I','O','U'],repeat=i):
                words.append(''.join(list(c)))
        words.sort()
        print(words.index(word)+1)
        return words.index(word)+1

    solution("I")

# 등비수열 공식 이용
#  1+5+5(2제곱)+...5(n-1)
class Test2:
    def solution(word):
        answer = 0
        for i, char in enumerate(word):
            coef = ((5 ** (5 - i) - 1) / (5 - 1))
            answer += coef * "AEIOU".index(char) + 1
        return answer