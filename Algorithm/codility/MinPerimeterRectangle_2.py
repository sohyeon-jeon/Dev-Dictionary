# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    answer = []
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            answer.append(2 * (i + (N // i)))
    print(answer)
    return min(answer)


solution(30)


"""
1 2 3 5 6 10 15 30
n=30
(1, 30): 둘레 62
(2, 15): 둘레 34
(3, 10): 둘레 26
(5, 6): 둘레 22
직사각형의 최소둘레 22 리턴
"""
