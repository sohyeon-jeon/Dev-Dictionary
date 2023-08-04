# 시간초과 -> O(n^2) , max함수도 O(n)의 시간 복잡도
def solution1(N, A):
    plus_count = [0] * N
    for i in range(len(A)):
        if A[i] == N + 1:
            _max = max(plus_count)
            plus_count = [_max] * N
        else:
            plus_count[A[i] - 1] += 1
    return plus_count


# 시간초과 77점 -> O(n^2) , plus_count = [max_count] * N 이거도 전체 다 리셋하므로 시간복잡도 O(n),
def solution2(N, A):
    plus_count = [0] * N
    max_count = 0

    for i in range(len(A)):
        if A[i] == (N + 1):
            plus_count = [max_count] * N
        else:
            plus_count[A[i] - 1] += 1
            max_count = max(max_count, plus_count[A[i] - 1])

    return plus_count


# m1,m2과 변수로 계산함
def solution(N, A):
    plus_count = [0] * N
    m1 = 0  # 다음 최댓값이 나오기 전까지의 최대값
    m2 = 0  # for문마다 최대값

    for i in range(len(A)):
        if A[i] == (N + 1):
            m1 = m2
        else:
            plus_count[A[i] - 1] = max(m1 + 1, plus_count[A[i] - 1] + 1)
            m2 = max(m2, plus_count[A[i] - 1])

    # 한번만 나온 값 대비
    for i, p in enumerate(plus_count):
        if p < m1:
            plus_count[i] = m1
    return plus_count


#   (3, 2, 2, 4, 2)
solution(5, [3, 4, 4, 6, 1, 4, 4])
