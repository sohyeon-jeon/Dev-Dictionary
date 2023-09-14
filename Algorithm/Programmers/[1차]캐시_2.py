"""
https://school.programmers.co.kr/learn/courses/30/lessons/17680
"""
from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    time = 0
    cache = deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        # 기존꺼가 원래 있으면 그 위치에서 지우고 뒤에 붙인다!
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        # 기존꺼가 cache에 없으면 앞에꺼를(오래된거) 지우고 뒤에 붙인다!
        #  maxlen=cacheSize 지정해서 앞에꺼 알아서 지워줌
        else:
            cache.append(city)
            time += 5
    return time


# 21
solution(
    3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
)
