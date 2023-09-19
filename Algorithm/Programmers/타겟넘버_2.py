"""
https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
"""
from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque([])
    q.append([numbers[0], 0])
    q.append([numbers[0] * (-1), 0])

    while q:
        v, level = q.popleft()
        level += 1
        if level < len(numbers):
            q.append([v + numbers[level], level])
            q.append([v - numbers[level], level])
        else:
            if v == target:
                answer += 1
    return answer


solution([1, 1, 1, 1, 1], 3)
