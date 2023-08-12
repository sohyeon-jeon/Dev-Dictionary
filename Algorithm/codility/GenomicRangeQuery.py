# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


# 62점 -> O(N * M) 시간초과
def solution1(S, P, Q):
    answer = []
    dna_dict = {"A": 1, "C": 2, "G": 3, "T": 4}
    for a, b in zip(P, Q):
        _min = 1e5
        for i in range(a, b + 1):
            _min = min(_min, dna_dict[S[i]])
        answer.append(_min)
    return answer


# 100점!! 시간복잡도 O(N + M) , 작은것 부터 있는지 확인
def solution(S, P, Q):
    answer = []
    for a, b in zip(P, Q):
        if "A" in S[a : b + 1]:
            num = 1
        elif "C" in S[a : b + 1]:
            num = 2
        elif "G" in S[a : b + 1]:
            num = 3
        elif "T" in S[a : b + 1]:
            num = 4
        answer.append(num)
    return answer


# A, C, G and T -> 1,2,3,4
# [2, 4, 1]
solution("CAGCCTA", [2, 5, 0], [4, 5, 6])
