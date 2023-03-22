'''
https://school.programmers.co.kr/learn/courses/30/lessons/159993
'''
from collections import deque

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def bfs(maps,x,y,end):
    n,m=len(maps),len(maps[0])
    visited=[[-1]*m for _ in range(n)]
    visited[x][y]=0
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        if maps[x][y]==end:
            return [visited[x][y],x,y]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==-1:
                    if maps[nx][ny]!='X':
                        visited[nx][ny]=visited[x][y]+1
                        queue.append((nx,ny))
    return None

def solution(maps):
    start_X,start_Y=0,0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=='S':
                start_X,start_Y=i,j

    s_l_distance=bfs(maps,start_X,start_Y,'L')
    if s_l_distance is None:
        return -1
    
    l_e_distance=bfs(maps,s_l_distance[1],s_l_distance[2],'E')
    if l_e_distance is None:
        return -1
    
    return s_l_distance[0]+l_e_distance[0]
      
solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])
# solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])

"""
따라서, 출발 지점에서 먼저 레버가 있는 칸으로 이동하여 레버를 당긴 후 미로를 빠져나가는 문이 있는 칸으로 이동하면 됩니다.
-> (Start~Lever)거리 + (Lever~End) 거리
"""