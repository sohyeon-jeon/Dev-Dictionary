"""
https://school.programmers.co.kr/learn/courses/30/lessons/12923
"""
import math


# n의 최대 약수를 찾는다.
def maxdivisor(n):
    if n == 1:
        return 0

    divisors = []
    for x in range(1, int(n**0.5) + 1):
        if n % x == 0:
            if x <= 1e7:
                divisors.append(x)
            if n // x <= 1e7 and n // x != n:
                divisors.append(n // x)

    return max(divisors)


def solution(begin, end):
    answer = [maxdivisor(n) for n in range(begin, end + 1)]
    return answer


# [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]
solution(1, 10)


# 실패 -> 약수 중 가장 큰 값 찾아서 graph의 max값으로 설정
def solution1(begin, end):
    arr = []
    graph = [0] * (end + 1)
    for i in range(1, int(math.sqrt(end)) + 1):
        if end % i == 0:
            arr.append(i)

    _max = end // arr[-1]

    for i in range(1, _max + 1):
        for j in range((begin * i) + i, end + 1, i):
            graph[j] = i
    return graph[1:]
