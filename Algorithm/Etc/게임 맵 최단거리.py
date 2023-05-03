'''
https://school.programmers.co.kr/learn/courses/30/lessons/1844
'''
# 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.

from collections import deque
# 1이면 갈 수 있고 0이면 벽
def solution(maps):
    n=len(maps)
    m=len(maps[0])
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]

    q=deque()
    q.append((0,0))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if maps[nx][ny]==0:
                continue
            if maps[nx][ny]==1:
                maps[nx][ny]=maps[x][y]+1
                q.append((nx,ny))

    # 도달할 수 없을 떄는 -1 리턴
    if maps[n-1][m-1]==1:
        return -1
    return maps[n-1][m-1]
        
# 11
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
