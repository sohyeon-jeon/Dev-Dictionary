"""
https://school.programmers.co.kr/learn/courses/30/lessons/43236
"""


def solution(distance, rocks, n):
    # 커트라인 최솟값 = 1
    left = 1
    # 커트라인 최댓값 = distance
    right = distance

    # 바위 위치를 정렬하고, 도착지점 append
    rocks.sort()
    rocks.append(distance)

    while left <= right:
        mid = (left + right) // 2
        # 제거한 바위 개수
        delete = 0
        # 이전 바위의 위치
        prev_rock = 0
        for rock in rocks:
            dist = rock - prev_rock
            # 거리가 커트라인 보다 작다면, 바위를 제거
            if dist < mid:
                delete += 1
                # 제거한 바위가 너무 많다면 break
                if delete > n:
                    break
            # 바위를 제거하지 않았다면, prev_rock을 갱신
            else:
                prev_rock = rock

        # 초과 제거한 경우 : 커트라인이 너무 높음
        if delete > n:
            right = mid - 1
        # 이하 제거한 경우 : 커트라인이 적절하거나 너무 낮음
        else:
            answer = mid
            left = mid + 1
    return answer


solution(25, [2, 14, 11, 21, 17], 2)
