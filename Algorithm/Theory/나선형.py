n=5
graph=[[0]*n for _ in range(n)]
now=[n//2,n//2]
num=1
graph[now[0]][now[1]]=num

def move(cnt,dx,dy,flag):
    global num
    for _ in range(cnt):
        now[0]+=dx
        now[1]+=dy
        
        if now[0]<0 or now[1]<0:
            break

        num+=1
        graph[now[0]][now[1]]=num


for i in range(1,n+1):
    if i%2!=0:
        move(i,0,-1,'left') 
        move(i,1,0,'down')
    else:
        move(i,0,1,'right')
        move(i,-1,0,'up')

print(graph)