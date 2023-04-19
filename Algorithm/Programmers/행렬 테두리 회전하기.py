'''
https://school.programmers.co.kr/learn/courses/30/lessons/77485
'''
def solution(rows, columns, queries):
    answer=[1e9]*len(queries)
    graph=[[0]*columns for _ in range(rows)]
    num=0

    for i in range(rows):
        for j in range(columns):
            num+=1
            graph[i][j]=num

    for idx,query in enumerate(queries):
        x1,y1,x2,y2=query
        # 시작값 변수 저장해두기
        a=graph[x2-1][y1-1]

        # 위쪽
        for x in range(x2-1,x1-1,-1):
            answer[idx]=min(answer[idx],a)
            b=graph[x-1][y1-1]
            graph[x-1][y1-1]=a
            a=b
        
        # 오른쪽
        for y in range(y1+1,y2+1):
            answer[idx]=min(answer[idx],a)
            b=graph[x1-1][y-1]
            graph[x1-1][y-1]=a
            a=b

        # 아래쪽
        for x in range(x1,x2):
            answer[idx]=min(answer[idx],a)
            b=graph[x][y2-1]
            graph[x][y2-1]=a
            a=b
        
        # 왼쪽
        for y in range(y2,y1,-1):
            answer[idx]=min(answer[idx],a)
            b=graph[x2-1][y-2]
            graph[x2-1][y-2]=a
            a=b
    return answer



