'''
https://school.programmers.co.kr/learn/courses/30/lessons/132265
'''
class test1:
    def solution(topping):
        answer = 0
        for i in range(len(topping)):
            if len(set(topping[:i+1]))==len(set(topping[i+1:])):
                answer+=1
        return answer
    
'''
set으로 중복제거 해서 비교하려고 했는데 시간초과 발생!
'''
from collections import Counter

class Test2:
    def solution(topping):
        answer=0
        one=Counter(topping)
        two=set()
        for t in topping:
            one[t]-=1
            two.add(t)
            if one[t]==0:
                del one[t]
            if len(one)==len(two):
                answer+=1
        return answer
    solution([1, 2, 1, 3, 1, 4, 1, 2])

'''
set+dictionary 이용
형(one)이 케이크를 모두 가져가고 동생(two)가 형꺼를 하나씩 빼는 설정
형과 동생이 가진 케이크 종류가 같으면 answer에 1 더하기
'''