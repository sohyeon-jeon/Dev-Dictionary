'''
https://school.programmers.co.kr/learn/courses/30/lessons/154540
'''
import sys 
sys.setrecursionlimit(10**5)

def solution(maps):
    answer = []
    global totalSum
    totalSum=0
    maps=[list(map) for map in maps]
    n=len(maps)
    m=len(maps[0])
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]

    def dfs(x,y):
        global totalSum
        maps[x][y]='X'
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if (0<=nx<n and 0<=ny<m) and maps[nx][ny]!='X':
                totalSum+=int(maps[nx][ny])
                dfs(nx,ny)

    for i in range(n):
        for j in range(m):
            if (0<=i<n and 0<=j<m) and maps[i][j]!='X':
                totalSum=int(maps[i][j])
                dfs(i,j)
                answer.append(totalSum)

   
    if not answer:
        answer.append(-1)
    return sorted(answer)
    


solution(["X591X","X1X5X","X231X", "1XXX1"])