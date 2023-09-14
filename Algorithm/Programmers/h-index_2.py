"""
https://school.programmers.co.kr/learn/courses/30/lessons/42747
"""


def solution(citations):
    citations.sort(reverse=True)
    for i, v in enumerate(citations):
        if i >= v:
            return i
    return len(citations)


# 3
solution([3, 0, 6, 1, 5])

"""
논문중 많이 인용된 순으로 정렬후, 인용수가 논문수와 같아지거나 작아질 때 h를 구할 수 있다.
논문 인용횟수(v)가 적어도 i편이 된다는 것!
"""
