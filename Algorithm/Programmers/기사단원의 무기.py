'''
https://school.programmers.co.kr/learn/courses/30/lessons/136798
'''

# 시간초과
class Test1:
    def solution(number, limit, power):
        answer = [0]*(number+1)    
        
        for i in range(1,number+1):
            for j in range(1,i+1):
                if i%j==0:
                    answer[i]+=1
        
        for i in range(len(answer)):
            if answer[i]>limit:
                answer[i]=power
            
        return sum(answer)

def get_cds(n, limit , power):
    cnt = 0
    for i in range(1, int(n**(1/2))+1): # ★포인트1. 제곱근만큼만 반복
        if n%i == 0:
            if i == n//i: # 제곱근일 경우 -> 1개만 카운트하기
                cnt += 1
            else:
                cnt += 2 # 제곱근이 아닐 경우, 2개 카운트 (i, n//i)
        if cnt > limit:  # ★포인트2. 소수의 개수가 limit를 넘어가면
            return power #            강제로 power만큼을 return 
    return cnt


def solution(number, limit, power):
    total=1
    for i in range(2,number+1):
        len_cds=get_cds(i, limit, power)
        total+=len_cds
    return total


solution(5, 3, 2)

'''
약수의 개수를 구하는 함수에서 시간초과를 줄이는 방법

1. for문을 돌릴때 제곱근까지 반복한다.
예를들어 18의 제곱근은 4.xxx가 나온다.
for문을 돌리면 1,2,3,4중에서
[1,2,3]이 18의 약수로 나온다.
18을 18의 약수들로 나눈 [18,9,6]도 카운트 된다.

2. 그리고 문제의 제한조건에서 약수의 개수가 특정 숫자를 넘어가면,
강제로 power만큼 고정하라고 한다.
for문을 돌릴 필요없이 강제로 power를 리턴하고 종료시킨다.
'''
