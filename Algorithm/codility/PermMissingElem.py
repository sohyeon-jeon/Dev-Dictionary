# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    n = len(A)
    # 0부터 n+1까지 헙
    con_sum = ((n + 1) * (n + 2)) // 2
    return con_sum - sum(A)


# 4
solution([2, 3, 1, 5])
