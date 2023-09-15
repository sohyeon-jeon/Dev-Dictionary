"""
https://school.programmers.co.kr/learn/courses/30/lessons/42862?language=python3
"""


def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생이 도난 당할 수 있음
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)

    for r in _reserve:
        if r - 1 in _lost:
            _lost.remove(r - 1)
        elif r + 1 in _lost:
            _lost.remove(r + 1)
    print(n - len(_lost))
    return n - len(_lost)


# 4
solution(5, [2, 4], [3])
