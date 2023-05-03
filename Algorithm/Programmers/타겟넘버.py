'''
https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
'''
from collections import deque


class Test1:
    def solution(numbers, target):
        answer = 0
        idx=0
        q=deque()
        q.append((numbers[0],idx))
        q.append((numbers[0]*(-1),idx))
        while q:
            num,idx=q.popleft()
            idx+=1
            if idx<len(numbers):
                q.append((num+numbers[idx],idx))
                q.append((num-numbers[idx],idx))
            else:
                if num==target:
                    answer+=1
        return answer
    
from itertools import product
# 
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    '''
    (1, -1) (1, -1) (1, -1) (1, -1) (1, -1)
    ->
    [(1, 1, 1, 1, 1), (1, 1, 1, 1, -1), (1, 1, 1, -1, 1), (1, 1, 1, -1, -1), (1, 1, -1, 1, 1), (1, 1, -1, 1, -1), (1, 1, -1, -1, 1), (1, 1, -1, -1, -1), (1, -1, 1, 1, 1), (1, -1, 1, 1, -1), (1, -1, 1, -1, 1), (1, -1, 1, -1, -1), (1, -1, -1, 1, 1), (1, -1, -1, 1, -1), (1, -1, -1, -1, 1), (1, -1, -1, -1, -1), (-1, 1, 1, 1, 1), (-1, 1, 1, 1, -1), (-1, 1, 1, -1, 1), (-1, 1, 1, -1, -1), (-1, 1, -1, 1, 1), (-1, 1, -1, 1, -1), (-1, 1, -1, -1, 1), (-1, 1, -1, -1, -1), (-1, -1, 1, 1, 1), (-1, -1, 1, 1, -1), (-1, -1, 1, -1, 1), (-1, -1, 1, -1, -1), (-1, -1, -1, 1, 1), (-1, -1, -1, 1, -1), (-1, -1, -1, -1, 1), (-1, -1, -1, -1, -1)]
    '''
    s = list(map(sum, product(*l)))
    return s.count(target)
    


solution([1, 1, 1, 1, 1],3)