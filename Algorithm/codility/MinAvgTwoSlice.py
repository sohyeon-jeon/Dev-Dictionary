def solution(A):
    min_avg = (A[0] + A[1]) / 2
    min_idx = 0
    for i in range(2, len(A)):
        avg_2 = (A[i - 1] + A[i]) / 2
        avg_3 = (A[i - 2] + A[i - 1] + A[i]) / 3
        if avg_2 < min_avg:
            min_avg = avg_2
            min_idx = i - 1
        if avg_3 < min_avg:
            min_avg = avg_3
            min_idx = i - 2
    return min_idx


solution([4, 2, 2, 5, 1, 5, 8])

"""
- a<=b일때 a와 b의 평균은 a이상이 된다.
- (a+b)<=(c+d)일때, (a,b)와 (c,d)의 평균은 (a+b)이상이 된다.
- (a,b,c,d)일 때 (a,b)와 (c,d)로 나누면 각각의 평균의 작은 값 이상이 된다.
=> 2개와 3개 슬라이스만 비교하면 된다.
"""
