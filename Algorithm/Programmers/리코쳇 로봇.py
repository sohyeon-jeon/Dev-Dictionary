"""
https://school.programmers.co.kr/learn/courses/30/lessons/169199
"""
from collections import deque


def bfs(board, start, end, m, n):
    distance = [[-1] * m for _ in range(n)]
    distance[start[0][0]][start[0][1]] = 0

    q = deque()
    q.append((start[0][0], start[0][1], 0))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, c = q.popleft()
        for d in range(4):
            nx = x
            ny = y

            # 장애물이나 맨 끝에 부딪힐 때까지 미끄러져 이동!!
            while (
                0 <= nx + dx[d] < n
                and 0 <= ny + dy[d] < m
                and board[nx + dx[d]][ny + dy[d]] != "D"
            ):
                nx += dx[d]
                ny += dy[d]
            # 방문하지 않았거나 더 적은 횟수로 이동할 수 있다면
            if distance[nx][ny] == -1 or distance[nx][ny] > c + 1:
                distance[nx][ny] = c + 1
                q.append((nx, ny, c + 1))
    return distance[end[0][0]][end[0][1]]


def solution(board):
    n = len(board)
    m = len(board[0])

    start = []
    end = []

    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start.append((i, j))
            elif board[i][j] == "G":
                end.append((i, j))

    return bfs(board, start, end, m, n)
