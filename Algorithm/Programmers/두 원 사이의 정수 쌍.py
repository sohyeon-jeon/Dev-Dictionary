"""
https://school.programmers.co.kr/learn/courses/30/lessons/181187
"""


def solution(r1, r2):
    answer = r2 - r1 + 1
    for n in range(r1, r2):
        answer += (2 * n) - 1

    return answer * 4


solution(2, 3)
