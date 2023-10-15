"""
https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""
from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    distance = [[-1] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((0, 0))
    distance[0][0] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if (
                0 <= nx < n
                and 0 <= ny < m
                and maps[nx][ny] != 0
                and distance[nx][ny] == -1
            ):
                distance[nx][ny] = distance[x][y] + 1

                q.append((nx, ny))
        x, y = nx, ny
    
    return distance[n-1][m-1]




solution(
    [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1],
    ]
)
"""
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
"""
