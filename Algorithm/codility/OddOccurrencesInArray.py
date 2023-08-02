from collections import Counter


# Counter 함수 사용
def solution(A):
    for k, v in Counter(A).items():
        if v % 2 != 0:
            return k


solution([9, 3, 9, 3, 9, 7, 9])
