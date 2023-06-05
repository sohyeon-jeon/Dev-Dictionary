'''
https://school.programmers.co.kr/learn/courses/30/lessons/12914
'''

# 런타임에러! 
class Test1:
    def solution(n):
        answer=[0]*(n+1)
        answer[1]=1
        answer[2]=2
        for i in range(3,n+1):
            answer[i]=answer[i-2]+answer[i-1]
        return answer[n]%1234567

# if문으로 n=1, n=2일 때를 추가했다. -> n=1, n=2일 경우 알고리즘 짤 필요도 없다
def solution(n):
    if n<3:
        return n
    answer=[0]*(n+1)
    answer[1]=1
    answer[2]=2
    for i in range(3,n+1):
        answer[i]=answer[i-2]+answer[i-1]
    return answer[n]%1234567

# 5
# solution(4)
# 3
solution(3)

'''
!!! 전형적인 dp문제

n=1
[1]

n=2
[1,1]
[2]

n=3
[1,1,1]
[1,2]
[2,1]

n=4
[1,1,1,1,1]
[1,2,1]
[1,1,2]
[2,1,1]
[2,2]
'''