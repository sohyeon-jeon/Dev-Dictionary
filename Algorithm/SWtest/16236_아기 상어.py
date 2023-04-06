"""
https://www.acmicpc.net/problem/16236
"""
from collections import deque

def bfs(x,y,shark_size):
    # 상어 현재 위치 0으로!
    graph[x][y]=0
    distance_graph=[[0]*n for _ in range(n)]
    queue=deque()
    queue.append((x,y))
    # 상어가 현재 위치에서 먹을 수 있는 물고기를 담을 배열
    fish_arr=[]

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            # 상어보다 물고기가 크면 못지나가요~
            if graph[nx][ny]>shark_size:
                continue
            # (칸이 빈 칸이거나, 상어의 크기보다 물고기의 크기가 작거나 크고) 방문한적이 없으면!!
            # 상어가 지나갈 수 있음
            if (graph[nx][ny]==0 or graph[nx][ny]<=shark_size) and distance_graph[nx][ny]==0:
                distance_graph[nx][ny]=distance_graph[x][y]+1
                queue.append((nx,ny))

    for i in range(n):
        for j in range(n):
            if 0<graph[i][j]<shark_size and distance_graph[i][j]!=0:
                fish_arr.append((i,j,distance_graph[i][j]))

    # 현재위치로부터의물고기까지거리, 맨 위, 맨 왼쪽 기준으로 정렬
    return sorted(fish_arr,key=lambda x: (x[2],x[0],x[1]))
    
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,-1,0,1]

eat=0
shark_size=2
distance=0

result=0

for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            x,y=i,j

while True:
    shark=bfs(x,y,shark_size)
    # 더 이상 먹을 물고기가 없으면 엄마 상어 소환!
    if len(shark)==0:
        break
    nx,ny,dist=shark[0]
    # 거리 누적
    result+=dist
    # 먹은 물고기 자리 빈칸 만들기
    graph[nx][ny]=0
    # 새로운 x,y
    x,y=nx,ny
    # 먹은 물고기+1
    eat+=1
    # 먹은 물고기와 상어크기가 같으면 아기 상어 몸집 키우기!
    if eat==shark_size:
        shark_size+=1
        eat=0

print(result)


