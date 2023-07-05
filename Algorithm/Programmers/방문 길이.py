'''
https://school.programmers.co.kr/learn/courses/30/lessons/49994
'''
def solution(dirs):
    point_set=set()
    cmd=['U','D','L','R']
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    x,y=0,0

    for d in dirs:
        for i in range(len(cmd)):
            if d==cmd[i]:
                nx=x+dx[i]
                ny=y+dy[i]
                if (-5<=nx<=5 and -5<=ny<=5):
                    if (x,y,nx,ny) not in point_set and (nx,ny,x,y) not in point_set:
                        point_set.add((x,y,nx,ny))
                    x,y=nx,ny
    
    return len(point_set)

# 1
solution("LRLRL")

'''
good
'''

