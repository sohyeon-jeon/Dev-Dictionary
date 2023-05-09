'''
https://school.programmers.co.kr/learn/courses/30/lessons/150369
'''
'''
그리디문제, 가장 먼 곳 부터 배달해야 최소거리로 배달할 수 있다.

'''
from itertools import zip_longest as zip
# zip_longest : 두 배열의 길이가 다를 때 사용
def solution(cap, n, deliveries, pickups):
    d=[]
    p=[]
    for i in range(len(deliveries)):
        d+=[i+1]*deliveries[i]
        p+=[i+1]*pickups[i]
    d.reverse()
    p.reverse()
    d=d[::cap]
    p=p[::cap]
    return 2*sum([max(x,y) for x,y in zip(d,p,fillvalue=0)])
