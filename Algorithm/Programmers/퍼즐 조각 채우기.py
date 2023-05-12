'''
https://school.programmers.co.kr/learn/courses/30/lessons/84021
'''
import copy

def dfs(board, x, y, position, n, num):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    result = [position]

    board[x][y] = 2  # 방문처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if board[nx][ny] == num:
                result += dfs(board, nx, ny, [position[0] + dx[i], position[1] + dy[i]], n, num)
    return result

def rotate(table):
    n=len(table)
    rotated=[[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1]=table[i][j]
    return rotated
            
            
def solution(game_board, table):
    answer = 0
    n=len(game_board)
    copy_game_board=copy.deepcopy(game_board)
    blank=[]
    
    for i in range(n):
        for j in range(n):
            if copy_game_board[i][j]==0:
                blank.append(dfs(copy_game_board,i,j,[0,0],n,0))
    
    for k in range(4):
        table = rotate(table)
        copy_table = copy.deepcopy(table)
        for i in range(n):
            for j in range(n):
                if copy_table[i][j] == 1:
                    block = dfs(copy_table, i, j, [0, 0], n, 1)
                    if block in blank:
                        blank.remove(block)
                        answer += len(block)
                        table = copy.deepcopy(copy_table)
                    else:
                        copy_table = copy.deepcopy(table)
    return answer

'''
1. game_board에서 빈칸의 좌표를 dfs로 구하고 해당 좌표를 0,0 위치를 기준으로 이동시킨다.
2. table에서 블록의 좌표를 dfs로 구하고 해당 좌표를 0,0 위치를 기준으로 이동시킨다.
3. 블록 좌표가 빈칸 좌표와 일치하면 빈칸 좌표를 지우고 이동칸만큼 answer에 더해준다.
4. 해당 블록 좌표는 더이상 사용하면 안되므로 table을 업데이트 시켜준다.
5. 만약 일치하지 않는다면 table을 원래대로 돌려놓는다.
2~5번 과정을 회전 횟수 4번만큼 반복한다.
'''