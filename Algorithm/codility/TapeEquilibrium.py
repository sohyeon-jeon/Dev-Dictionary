# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


# 시간초과!! -> 문제 > for문 돌때마다 합 계산...
def solution1(A):
    answer = 1e9
    for i in range(1, len(A)):
        answer = min(answer, abs(sum(A[:i]) - sum(A[i:])))
    return answer


def solution(A):
    answer = 1e9
    # 누적합 리스트
    cumulative_sum = [0] * (len(A) + 1)
    for i in range(len(A)):
        cumulative_sum[i + 1] = cumulative_sum[i] + A[i]

    for i in range(1, len(A)):
        answer = min(
            answer, abs(cumulative_sum[i] - (cumulative_sum[-1] - cumulative_sum[i]))
        )
    return answer


# 1
# |3 − 10| = 7
solution([3, 1, 2, 4, 3])
