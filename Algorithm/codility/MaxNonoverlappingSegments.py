# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, B):
    N = len(A)
    if N == 0:
        return 0
    if N == 1:
        return 1

    point = []
    for s, e in zip(A, B):
        point.append((s, e))
    # 끝 점을 기준으로 먼저 정렬
    point.sort(key=lambda x: (x[1], x[0]))

    end_point = point[0][1]
    cnt = 1

    # 내가 가지고 있는 end_point보다 새로운 시작점이 작으면 안겹침
    for i in range(1, N):
        if end_point < point[i][0]:
            end_point = point[i][1]
            cnt += 1
    return cnt


# 최대한 많은 수의 비겹침 세그먼트 수
# 3
solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10])
"""

"""
