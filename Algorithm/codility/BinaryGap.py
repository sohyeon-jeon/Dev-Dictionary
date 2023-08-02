def solution1(N):
    answer = 0
    binary = ""
    while N > 0:
        N, mod = divmod(N, 2)
        binary += str(mod)
    binary = binary[::-1]

    one_arr = []
    for i, v in enumerate(binary):
        if v == "1":
            one_arr.append(i)

    if len(one_arr) <= 1:
        return 0

    for i in range(1, len(one_arr)):
        answer = max(answer, one_arr[i] - one_arr[i - 1] - 1)
    return answer


# 더 깔끔하게 정리
def solution2(N):
    binary_gap = []
    gap = 0
    while N > 0:
        N, mod = divmod(N, 2)
        if mod == 1:
            binary_gap.append(gap)
            gap = 0
        else:
            gap += 1
    binary_gap.append(gap)
    binary_gap[0] = 0
    return max(binary_gap)


# 529
solution2(32)
