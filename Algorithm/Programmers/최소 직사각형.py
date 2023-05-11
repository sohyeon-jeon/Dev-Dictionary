'''
https://school.programmers.co.kr/learn/courses/30/lessons/86491
'''
def solution(sizes):
    answer = 0
#     가로, 세로 바꿀 수 있음(회전가능)
# 명함에서 가로,세로 중 큰 것을 가로로 하고 세로 중에서 가장 큰 값 출력
    w=[]
    h=[]
    for a,b in sizes:
        w.append(max(a,b))
        h.append(min(a,b))
    return max(w)*max(h)
