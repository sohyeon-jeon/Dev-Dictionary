"""
source : 2018 E 기업 알고리즘 대회
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단, 두 번째 연산은 n이 k로 나누어떨어질 때만 선택할 수 있다.
1. n에서 1을 뺀다.
2. n을 k로 나눈다.
n과 k가 주어질 때 n이 1이 될때까지 1번 혹은 2번의 과정을 수행해야하는 최소 횟수를 구하여라.


입력 조건>
2<=n<=100,000, 2<=k<=100,000

입력>
25 5
출력>
2
"""
def test1():
    n,k=map(int,input().split())

    count=0
    '''
    최대한 많이 나누어서 과정 횟수를 줄일 수 있다.
    '''

    while True:
        if n==1:
            break
        else:
            if n%k==0:
                n//=k
                count+=1
            else:
                n-=1
                count+=1
    print(count)

def test2():
    n,k=map(int,input().split())
    result=0

    while n>=k:
        # n이 k로 나누어떨어지지 않는다면 계속 뺀다.
        while n%k!=0:
            n-=1
            result+=1
        # k로 나누기
        n//=k
        result+=1

    # 남은 수에 대해 1씩 빼기
    while n>1:
        n-=1
        result+=1

    print(result)
