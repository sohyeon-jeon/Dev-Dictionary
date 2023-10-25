"""
https://school.programmers.co.kr/learn/courses/30/lessons/148652#
"""


def f(n, k):
    if n == 1:
        return k if k <= 2 else k - 1

    div = 5 ** (n - 1)  # 나눌 수, 항상 5개의 구역으로 나눌 것
    mul = 4 ** (n - 1)  # 1의 개수
    loc = k // div

    if loc < 2:
        return mul * loc + f(n - 1, k - (div * loc))
    elif loc == 2:
        return mul * loc
    else:
        return mul * (loc - 1) + f(n - 1, k - (div * loc))


def solution(n, l, r):
    return f(n, r) - f(n, l - 1)


solution(2, 4, 17)
"""
n=0 -> 1
n=1 -> 11011
n=2 -> 11011 11011 00000 11011 11011 -> 4/4/0/4/4
n=3 -> 1101111011000001101111011 ... 125가지 -> 16/16/0/16/16

* 5부분으로 나누어 재귀적 호출
"""
