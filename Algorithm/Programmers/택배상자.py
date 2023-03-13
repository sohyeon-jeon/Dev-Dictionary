'''
https://school.programmers.co.kr/learn/courses/30/lessons/131704
'''

def solution(order):
    cnt=0
    i=1
    stack=[]
    while i<=len(order):
        stack.append(i)
        while stack and stack[-1]==order[cnt]:
            cnt+=1
            stack.pop()
        i+=1
    return cnt
solution([4, 3, 1, 2, 5])

'''
while문과 변수를 이용해 문제를 해결하는 방법도 공부하자!
'''