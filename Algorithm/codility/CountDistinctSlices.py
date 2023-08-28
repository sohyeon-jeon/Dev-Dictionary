def solution(M, A):
    N = len(A)
    seen = [False] * (M + 1)  # 숫자 등장 여부를 저장하는 배열
    distinct_slices = 0
    left = 0

    for right in range(N):
        # 중복된 숫자가 있으면 left 포인터를 증가시켜 중복구간은 건너뛴다.
        while seen[A[right]]:
            seen[A[left]] = False
            left += 1

        seen[A[right]] = True
        distinct_slices += right - left + 1

        if distinct_slices > 1000000000:
            return 1000000000

    return distinct_slices


solution(6, [3, 4, 5, 5, 2])
