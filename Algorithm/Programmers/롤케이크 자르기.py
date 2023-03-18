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

'''
set+dictionary 이용
형(one)이 케이크를 모두 가져가고 동생(two)가 형꺼를 하나씩 빼는 설정
형과 동생이 가진 케이크 종류가 같으면 answer에 1 더하기
'''

'''
Test1 실행시간: 0.00010609626770019531
Test2 실행시간: 7.295608520507812e-06

Test2가 Test1보다 빠른 이유
1. Test1 : 중복을 제거하기 위해 set을 사용하여 slicing 연산으로 중복을 제거한다.
이 때 중복을 제거하려면, 모든 원소를 순회하며 중복을 제거하기 때문에 시간복잡도가 O(n2)이다.
2. Test2 : Counter와 set을 이용해 중복을 미리 제거한다. 그리고 배열을 순회하며 중복을 제거한다.
이 때 시간복잡도는 O(n)이다.
'''