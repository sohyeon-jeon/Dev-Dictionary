# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    answer = 0
    if int(N**0.5) * int(N**0.5) == N:
        answer = -1

    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            answer += 2
    return answer


"""
- N의 제곱근까지만 반복한다. 대칭적으로 약수가 분포하기 때문에 answer+=2
- 제곱근이 N과 같으면, N은 제곱수이므로 약수의 개수는 1개 감소 (EX>16)
1 2 4 8 16
"""

"""
양의 정수 인수 개수를 찾는 효율적인 알고리즘
"""
# I > 1, 2, 3, 4, 6, 8, 12, 24
# O >8
solution(24)

"""
O(sqrt(N))
"""
