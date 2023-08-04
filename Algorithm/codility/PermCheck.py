def solution(A):
    n = len(A)
    check = [0] * (n + 1)
    for a in A:
        # 범위 벗어나면 안됨
        if a < 1 or a > n:
            return 0
        # 이미 존재하면 안됨
        elif check[a] == 1:
            return 0
        check[a] = 1
    return 1


# 1
aa = solution([4, 1, 3, 2])
print(aa)
# 0
# solution([4, 1, 3])
