'''
https://school.programmers.co.kr/learn/courses/30/lessons/42578
'''
from collections import defaultdict

def solution(clothes):
    answer = 1
    clothesCnt=defaultdict(int)
    for a,b in clothes:
        clothesCnt[b]+=1
    
    for v in clothesCnt.values():
        answer*=(1+v)

    return answer-1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])

'''
옷의 종류가 2개이고 각각의 개수가 a,b라면?
a,b,ab -> (a+b)+(ab)

옷의 종류가 3개이고 각각의 개수가 a,b라면?
(a+b+c)+(ab+bc+ca)+(abc)가지
(x+a)(x+b)(x+c) = x3 + (a+b+c)x2 + (ab+bc+ca)x + (abc) 
x=1대입 
x3은 정답에 포함되지 않으니 1 빼주기



'''