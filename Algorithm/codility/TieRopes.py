"""
https://app.codility.com/programmers/lessons/16-greedy_algorithms/
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(K, A):
    rope_length = 0
    cnt = 0
    for length in A:
        rope_length += length
        if rope_length >= K:
            cnt += 1
            rope_length = 0
    return cnt


# 3
# 주어진 정수 K에 대한 목표는 로프를 가능한 한 많이 매달아서 길이가 K 이상인 로프의 개수를 최대화
solution(4, [1, 2, 3, 4, 1, 1, 3])
"""
내가 이해를 못하는건가..문제 설명 예시가 이상한 것 같다..

"""
