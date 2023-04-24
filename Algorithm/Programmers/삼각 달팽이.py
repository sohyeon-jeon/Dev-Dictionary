class Test1:
    def solution(n):
        answer = []
        graph=[[-1]*n for _ in range(n)]

        x,y=-1,0
        d=0
        num=0
        # 아래,오른쪽,대각선
        dx=[1,0,-1]
        dy=[0,1,-1]

        while True:
            if n==0:
                break
            
            # n=이 4이면 삼각형 모양으로 4->3->2->1로 감
            for _ in range(n):
                num+=1
                nx=x+dx[d]
                ny=y+dy[d]
                graph[nx][ny]=num
                x,y=nx,ny
            
            d+=1
            n-=1
            if d%3==0:
                d=0

        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j]!=-1:
                    answer.append(graph[i][j])


        return answer

    solution(4)

