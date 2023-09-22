"""
https://school.programmers.co.kr/learn/courses/30/lessons/131704
"""


def solution(order):
    cnt = 0
    stack = []
    for i in range(1, len(order) + 1):
        stack.append(i)
        while stack and stack[-1] == order[cnt]:
            stack.pop()
            cnt += 1
    return cnt


solution([4, 3, 1, 2, 5])
