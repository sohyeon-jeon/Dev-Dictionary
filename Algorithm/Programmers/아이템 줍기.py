from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # 제한사항에서 모든 좌표값은 1 이상 50 이하라고 했고 2배의 좌표를 그려야 하므로 102*102 크기의 2차원 배열 선언
    field = [[-1] * 102 for i in range(102)]
    
    # 직사각형 그리기
    for r in rectangle:
    	# 모든 좌표값 2배
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        # x1부터 x2, y1부터 y2까지 순회
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
            	# x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 테두리일 때 1로 채움
                elif field[i][j] != 0:
                    field[i][j] = 1
    print(field)
                    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 큐에 캐릭터 출발지점 추가 & 최단거리를 적어줄 visited 배열 선언
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited = [[1] * 102 for i in range(102)]
    
    while q:
        x, y = q.popleft()
        # 도착한 곳이 아이템이 있는 장소라면 현재의 최단거리(나누기 2)를 answer로 하고 while문을 빠져나옴
        if x == itemX * 2 and y == itemY * 2:
            return visited[x][y] // 2
        # 아니라면 상하좌우 네 방향을 체크하면서
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 현재 좌표가 테두리이고 아직 방문하지 않은 곳이라면 q에 추가 후 visited 최단거리로 갱신
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8)

'''
[0, 1, 1, 0] 
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 1, 1, 0]

[0, 0, 4, 0]
[0, 0, 3, 0]
[0, 0, 2, 0]
[0, s, 1, 0]

[0, 5, 6, 0]
[0, 4, 3, 0]
[0, 0, 2, 0]
[0, s, 1, 0]

모든 직사각형의 좌표를 2배 해주어야 한다.
ㄷ자 모양의 경우, 테두리를 따라 그림ㄴ ㅁ처럼 인식되어 착오가 있다.

'''