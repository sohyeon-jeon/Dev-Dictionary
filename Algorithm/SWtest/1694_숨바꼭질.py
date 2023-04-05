'''
https://www.acmicpc.net/problem/1697
'''
from collections import deque

def dfs():
    q=deque([n])
    while q:
        x=q.popleft()
        if x == k:
            print(dist[x])
            break
        for i in (x-1,x+1,x*2):
            if 0<=i<=max and dist[i]==0:
                dist[i]=dist[x]+1
                q.append(i)

n,k=map(int,input().split())
max=10**5
dist=[0]*(max+1)

dfs()