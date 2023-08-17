"""
https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/
"""
from math import gcd


# timeout error 50점
def solution1(N, M):
    stack = [0]
    while True:
        i = stack[-1]
        choco = (i + M) % N
        if choco not in stack:
            stack.append(choco)
        else:
            return len(stack)


# timeout error 87점
def solution2(N, M):
    if N < M:
        return 1

    i = 1
    while True:
        if (N * i) % M == 0:
            N *= i
            break
        i += 1

    return N // M


def solution(N, M):
    # 최대공약수 이용
    return N // gcd(N, M)


solution(10, 4)

"""
0 4 8 2 6 
20
"""
