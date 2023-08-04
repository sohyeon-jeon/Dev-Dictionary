# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


#  0 ≤ P < Q < N
def solution(A):
    zero = 0
    passing_car = 0
    for car in A:
        if car == 0:
            zero += 1
        else:
            passing_car += zero
            if passing_car > 1e9:
                return -1
    return passing_car


solution([0, 1, 0, 1, 1])
