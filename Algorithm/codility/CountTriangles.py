def solution(A):
    N = len(A)
    if N < 3:
        return 0

    A.sort()
    count = 0

    for r in range(2, N):
        p = 0
        q = r - 1

        while p < q:
            if A[p] + A[q] > A[r]:
                count += q - p
                q -= 1
            else:
                p += 1

        if count > 1000000000:
            return 1000000000

    return count


# A[P] + A[Q] > A[R],
# 4 리턴
# (0, 2, 4), (0, 2, 5), (0, 4, 5) 및 (2, 4, 5)
solution([10, 2, 5, 1, 8, 12])

"""
1 2 5 8 12 10
"""
