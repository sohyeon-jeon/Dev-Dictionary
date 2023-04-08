'''
왼쪽1-아래쪽1-오른쪽2-위쪽2-왼쪽3-아래쪽3....
왼쪽,아래쪽 -> 홀수번만큼 진행 / 오른쪽,위쪽 -> 짝수번만큼 진행

미리 비율을 설정하고, 범위가 벗어나면 정답값에 누적하고, 범위안에 들어오면 해당 좌표의 모래값을 업데이트 한다.
'''
n=int(input())
desert=[list(map(int,input().split())) for _ in range(n)]
# 밖으로 나간 모래양
answer=0
# 현재 x,y 좌표
now=[n//2,n//2]

# 모래 퍼지는 비율 미리 설정
left = [(-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01), (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (0, -2, 0.05), (0, -1, 0)] 
right = [(x, -y, z) for x, y, z in left] #오른쪽방향으로 퍼질때 
down = [(-y, x, z) for x, y, z in left] #아래쪽 방향으로 퍼질때 
up = [(-x, y, z) for x, y, z in down]  #위쪽방향으로 퍼질때 

rate={'left':left,'right':right,'down':down,'up':up}

def move(cnt,dx,dy,direction):
    global answer
    for _ in range(cnt):
        # 현재 좌표 업데이트
        now[0],now[1]=now[0]+dx, now[1]+dy
        # 회오리를 돌다가 끝나는 경우
        if now[0]<0 or now[1]<0:
            break
        
        # 모래가 퍼진값을 누적한 양
        spreads=0
        for dx,dy,r in rate[direction]:
            nx,ny=now[0]+dx,now[1]+dy
            # 퍼지지 않는 모래는 현재 자리에 누적
            if r==0:
                sand=desert[now[0]][now[1]]-spreads
            # 퍼지는 모래값 계산
            else:
                sand=int(desert[now[0]][now[1]]*r)

            if 0<=nx<n and 0<=ny<n:
                desert[nx][ny]+=sand #
            else:
                answer+=sand # 범위밖 : 정답 누적 업데이트
            spreads+=sand #현재자리 계산을 위한 퍼지는 모래의 누적값

for i in range(1,n+1):
    if i%2!=0:
        move(i,0,-1,'left') 
        move(i,1,0,'down')
    else:
        move(i,0,1,'right')
        move(i,-1,0,'up')

print(answer)



