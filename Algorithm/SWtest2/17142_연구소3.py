"""
https://www.acmicpc.net/problem/17142
"""
from collections import deque

def combinations(array,r):
    for i in range(len(array)):
        if r==1:
            yield [array[i]]
        else:
            for next in combinations(array[i+1:],r-1):
                yield [array[i]]+next

def bfs(active):
    result=0
    visited=[[-1]*n for _ in range(n)]

    queue=deque()
    
    # 활성화된 바이러스 담은 후 방문처리
    for x,y in active:
        queue.append((x,y))
        visited[x][y]=0

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                
                if graph[nx][ny]==0 and visited[nx][ny]==-1:
                    queue.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1 
                    result=max(result,visited[nx][ny])
                # 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.
                # 지나다닐 순 있다
                elif graph[nx][ny]==2 and visited[nx][ny]==-1:
                    queue.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1 

    # if list(sum(visited, [])).count(-1) != wall:
    #     return inf

    not_visited=0
    for i in range(n):
        not_visited+=visited[i].count(-1)
    if not_visited!=wall:
        return inf
    return result

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

inf = 99999
wall=0
virus=[]
ans = inf

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            wall+=1
        elif graph[i][j]==2:
            virus.append((i,j))

# 바이러스 M개 조합(활성화) 생성
for active in combinations(virus,m):
    ans = min(ans, bfs(active))

print(ans if ans != inf else -1)

"""
BFS+조합
"""

