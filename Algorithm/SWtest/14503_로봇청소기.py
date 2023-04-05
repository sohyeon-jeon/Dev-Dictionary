def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

def vacuum(x, y):
    chk[y][x] = 1
    cnt = 1
    turn_time = 0
    while True:
        turn_left()
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if status[ny][nx] == 0 and chk[ny][nx] == 0:  # 아직 청소하지 않은 빈 공간이 존재한다면,
            chk[ny][nx] = 1
            cnt += 1
            x, y = nx, ny
            turn_time = 0
            continue
        else:  # 그렇지 않을 경우,
            turn_time += 1

        if turn_time == 4:  # 1번으로 돌아가거나 후진하지 않고 2a 단계가 연속으로 네 번 실행되었을 경우,
            nx = x - dx[d]
            ny = y - dy[d]
            if status[ny][nx] == 0:
                x, y = nx, ny
            else:
                break
            turn_time = 0
    return cnt


n, m = map(int, input().split())
r, c, d = map(int, input().split())
status = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

chk = [[0]*m for _ in range(n)]
cnt = vacuum(c, r)
print(cnt)