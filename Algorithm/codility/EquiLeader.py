'''
https://app.codility.com/demo/results/trainingP2GJJW-NS5/
'''
from collections import Counter,defaultdict
def solution(A):
    answer=0
    N=len(A)
    leader=0
    left_dict=defaultdict(int)
    right_dict=Counter(A)

    # 리더 찾기
    for k,v in right_dict.items():
        if v>=(N//2):
            leader=k

    for i in range(N):
        left_dict[A[i]]+=1
        right_dict[A[i]]-=1
        if left_dict[leader]>((i+1)//2) and right_dict[leader]>((N-i-1)//2):
            answer+=1
    return answer

'''
처음에 문제를 이해하지 못해 잘못된 방법으로 풀고있었다.
문제 잘 읽자!
'''
