"""
https://school.programmers.co.kr/learn/courses/30/lessons/42885
"""

"""
이중 투포인터 이용
"""


def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    return answer


solution([70, 50, 80, 50], 100)
