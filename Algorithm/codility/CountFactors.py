import math
def solution(N):
    answer=0
    sqrtN=int(math.sqrt(N))
    if sqrtN * sqrtN == N:
        answer-=1
    for i in range(1, sqrtN + 1):
        if N%i==0:
            answer+=2
    return answer

'''
양의 정수 인수 개수를 찾는 효율적인 알고리즘
'''