# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    A = sorted(list(set(A)))
    num = 1
    for a in A:
        if a > 0:
            if a != num:
                break
            else:
                num += 1
    return num


# 5
solution([0])
"""
[1, 3, 6, 4, 1, 2] -> 5
[1,2,3] ->4
[-1,-3] -> 1
"""
