n=6
graph=[[0]*n for _ in range(n)]

num=0

if n%2==0:
    cnt=n//2
else:    
    cnt=(n//2)+1

for i in range(cnt):
    # 우
    for ny in range(i,n-i):
        num+=1
        graph[i][ny]=num

    # # 하
    for nx in range(i+1,n-i):
        num+=1
        graph[nx][n-(i+1)]=num

    # # 좌
    for ny in range(n-i-2,i-1,-1):
        num+=1
        graph[n-(i+1)][ny]=num

    # 상
    for nx in range(n-i-2,i,-1):
        num+=1
        graph[nx][i]=num

print(graph)

    
 


