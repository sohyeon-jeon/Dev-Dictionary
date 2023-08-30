def solution(A):
    A.sort()
    left = 0
    right = len(A) - 1

    min_abs = float("inf")

    while left <= right:
        sum = A[left] + A[right]
        min_abs = min(min_abs, abs(sum))

        if sum <= 0:
            left += 1
        else:
            right -= 1

    return min_abs


ㄴ
# 이중 투포인터 이용
# 절대값 합 중 최소 리턴
solution([-8, 4, 5, -10, 3])
