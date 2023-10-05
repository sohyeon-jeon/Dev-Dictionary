"""
https://school.programmers.co.kr/learn/courses/30/lessons/43238
"""


def solution(n, times):
    answer = 0
    # 최적의상황 left, 최악의 상황 right
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2

        # 심사한 사람 수
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break

        # 심사한 사람 수가 심사해야하는 사람수보다 많으면
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


# 28
solution(6, [7, 10])
"""
입력값이 크고 특정값을 찾아야하는 문제라면 이분탐색을 의심해보자.
1,000,000,000
"""
