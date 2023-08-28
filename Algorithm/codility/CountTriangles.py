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
                # p와 q사이 가능한 조합 모두 더해준다
                count += q - p
                # q를 왼쪽으로 이동하여 다음으로 작은 값 확인
                q -= 1
            else:
                # p를 오른쪽으로 이동하여 다음으로 큰 p값 확인
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
