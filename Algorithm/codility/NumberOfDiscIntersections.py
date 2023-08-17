def solution(A):
    n = len(A)
    start_point = [0] * n
    end_point = [0] * n
    for i in range(n):
        start_point[i] = i - A[i]
        end_point[i] = i + A[i]
    print(start_point)
    print(end_point)


solution([1, 5, 2, 1, 4, 0])
