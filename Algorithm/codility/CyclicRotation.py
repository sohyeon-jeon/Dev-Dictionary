"""
https://app.codility.com/demo/results/training4JDRDB-YTD/
"""


def solution1(A, K):
    # Implement your solution here
    for _ in range(K):
        if len(A) >= 1:
            A = [A[-1]] + A[:-1]
    return A


# 좀 더 나아진 풀이..
def solution(A, K):
    if not A:
        return A
    K %= len(A)
    return A[-K:] + A[:-K]


# [9, 7, 6, 3, 8]
solution([3, 8, 9, 7, 6], 3)
