'''
https://school.programmers.co.kr/learn/courses/30/lessons/138476
'''
from collections import Counter

def solution(k, tangerine):
    answer = 0
    tang_counter=sorted(Counter(tangerine).items(),key=lambda x:-x[1])
    for tang in tang_counter:
        value=tang[1]
        if k<=0:
            return answer
        k-=value
        answer+=1
    return answer

solution(4,[1, 3, 2, 5, 4, 5, 2, 3])

'''
collections.Counter 함수를 사용해서, 리스트 내에 원소가 몇 개 있는지 파악하고 값을 기준으로 내림차순 정렬!
다른 종류의 수를 최소화하기 위해서는, 크기별로 분류했을 때 종류가 많은 사과부터 k에서 빼야 한다!
그래서 k가 0이하가 되었을때 answer(사과 종류의 최솟값)을 return 해주면 된다!   
'''