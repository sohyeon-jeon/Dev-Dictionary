"""
https://school.programmers.co.kr/learn/courses/30/lessons/154540
"""
import sys

sys.setrecursionlimit(10**5)


def solution(maps):
    answer = []
    # 함수와 내부에서 각자 수정하기 위해 함수 외부와 내부에 둘 다 global 선언
    global total
    total = 0
    maps = [list(map) for map in maps]
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def dfs(x, y):
        global total
        # 방문 처리
        maps[x][y] = "X"
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if (0 <= nx < n and 0 <= ny < m) and maps[nx][ny] != "X":
                total += int(maps[nx][ny])
                dfs(nx, ny)

    for i in range(n):
        for j in range(m):
            if (0 <= i < n and 0 <= j < m) and maps[i][j] != "X":
                total = int(maps[i][j])
                dfs(i, j)
                answer.append(total)

    if not answer:
        answer.append(-1)
    return sorted(answer)


solution(["X591X", "X1X5X", "X231X", "1XXX1"])
