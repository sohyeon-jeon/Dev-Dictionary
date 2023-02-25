"""
https://school.programmers.co.kr/learn/courses/30/lessons/17680
캐시 교체 알고리즘 LRU((Least Recently Used) 사용
"""

from collections import deque

def test1():
    def solution(cacheSize, cities):
        answer = 0
        dq=deque()
            
        for city in cities:
            city=city.lower()
            # dq에 이미 있는 경우에는 기존의 것을 삭제 후, 맨 뒤로 이동(최근 들어온 데이터로 만들어줌)
            if city in dq:
                dq.remove(city)
                dq.append(city)
                answer+=1
            # dq에 없는 경우
            else:
                # 입력 조건을 보면  0 ≦ cacheSize ≦ 30 이다. 
                # 즉 0일때도 고려해야함.
                if cacheSize==0:
                    answer+=5
                # 맨 앞(제일 오래된)것 꺼내고 뒤로 city 붙이기
                elif len(dq)==cacheSize and len(dq)>0:
                    dq.popleft()
                    dq.append(city)
                    answer+=5
                # 뒤로 append~
                else:
                    dq.append(city)
                    answer+=5
        
        return answer
    solution(2,	["Jeju", "Pangyo", "NewYork", "newyork"])


def test2():
    def solution(cacheSize, cities):
        import collections
        cache = collections.deque(maxlen=cacheSize)
        time = 0
        for i in cities:
            s = i.lower()
            if s in cache:
                cache.remove(s)
                cache.append(s)
                time += 1
            else:
                cache.append(s)
                time += 5
        return time
