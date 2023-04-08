N = 5
board = [[i * N + j for j in range(N)] for i in range(N)]
 
 
def rotate45():
    # 시계방향으로 배열을 45도 회전하는 함수
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[N - j - 1][i]
    return new_board
 
 
print("원본")
for row in board:
    print(row)
print()
 
print("시계방향 45도 회전")
rotated = rotate45()
for row in rotated:
    print(row)
 