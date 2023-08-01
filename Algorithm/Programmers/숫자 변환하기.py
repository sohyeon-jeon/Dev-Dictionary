"""
https://school.programmers.co.kr/learn/courses/30/lessons/154538
"""
MAX = 1_000_000
INF = float("inf")


def solution(x, y, n):
    dp = [INF] * (MAX + 1)
    dp[x] = 0

    for i in range(x, y):
        if dp[y] != INF:
            return dp[y]

        for new_n in (i + n, 2 * i, 3 * i):
            if MAX < new_n:
                continue

            dp[new_n] = min(dp[new_n], dp[i] + 1)

    return dp[y] if dp[y] != INF else -1
