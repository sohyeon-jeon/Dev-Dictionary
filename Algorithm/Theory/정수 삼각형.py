"""
https://school.programmers.co.kr/learn/courses/30/lessons/43105
"""
from collections import defaultdict


def solution(triangle):
    answer = 0
    dp = defaultdict(int)
    dp[(0, 0)] = triangle[0][0]

    for x in range(1, len(triangle)):
        for y in range(len(triangle[x])):
            dp[(x, y)] = triangle[x][y] + max(dp[(x - 1, y - 1)], dp[(x - 1, y)])

    return max(dp.values())


# 30
solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
