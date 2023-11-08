def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (
                    dp[i - 1][j] + dp[i][j - 1]
                ) % 1000000007  # 나머지 연산을 추가하여 오버플로우 방지

    return dp[n][m]


#  1,000,000,007로 나눈 나머지
# 4
solution(4, 3, [[2, 2]])
