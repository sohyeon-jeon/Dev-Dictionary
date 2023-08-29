"""
https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/
"""


def solution(A):
    N = len(A)
    prefix_sum = [0] * N
    suffix_sum = [0] * N

    for i in range(1, N):
        # 0보다 작으면 합산하지 않는다.
        prefix_sum[i] = max(prefix_sum[i - 1] + A[i], 0)

    # prefix_sum=[0, 2, 8, 7, 11, 16, 15, 17]

    for i in range(N - 1, 0, -1):
        suffix_sum[i - 1] = max(suffix_sum[i] + A[i - 1], 0)

    # suffix_sum=[19, 16, 14, 8, 9, 5, 0, 0]

    max_double_slice = 0

    for i in range(1, N - 1):
        max_double_slice = max(max_double_slice, prefix_sum[i - 1] + suffix_sum[i + 1])

    return max_double_slice


solution([3, 2, 6, -1, 4, 5, -1, 2])
"""
X,Y,Z가 있을 때, Y를 기준으로 좌측값과 우측값을 더했을 때 최대값을 리턴하면 된다.

3 5 11 10 14 19 18 20
17리턴
double slice (0, 3, 6), 합은 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), 합은 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), 합은 0.
"""
