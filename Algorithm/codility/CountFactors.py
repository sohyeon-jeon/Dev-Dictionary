import math


def solution(N):
    answer = 0
    sqrtN = int(math.sqrt(N))
    if sqrtN * sqrtN == N:
        answer -= 1
    for i in range(1, sqrtN + 1):
        if N % i == 0:
            print(i)
            answer += 2

    return answer


solution(10)
"""
- N의 제곱근까지만 반복한다. 
- 제곱근이 N과 같으면, N은 제곱수이므로 약수의 개수는 1개 감소
"""

"""
양의 정수 인수 개수를 찾는 효율적인 알고리즘
"""
