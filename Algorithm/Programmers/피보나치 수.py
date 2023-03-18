'''
https://school.programmers.co.kr/learn/courses/30/lessons/12945
'''
class Test1:
    def fibonacci(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return fibonacci(n-1)+fibonacci(n-2)

    def solution(n):
        return fibonacci(n%1234567)
    '''
    "시간 초과" OR "런타임 에러"
    일부 언어는 재귀 호출을 할 수 있는 횟수가 정해져 있고, 횟수를 넘어 재귀 호출을 하면 런타임 에러를 내도록 설계되어 있습니다.
    '''
   
class Test2:
    def solution(n):
        fib=[0,1]
        for i in range(2,n+1):
            fib.append((fib[i-1]+fib[i-2])%1234567)
        return fib[n]
    '''
    동적 계획법(Dynamic Programming)
    : 하나의 큰 문제를 여러 개의 작은 문제로 나누어서 그 결과를 저장하여 다시 큰 문제를 해결할 때 사용
    : 기억하며 풀기
    : 재귀 사용시 작은 문제들이 여러 번 반복되어 비효율적인 계산이 될 수 있다. 그래서 재귀 문제를 해결하기 위해 DP를 많이 사용한다.
    '''


