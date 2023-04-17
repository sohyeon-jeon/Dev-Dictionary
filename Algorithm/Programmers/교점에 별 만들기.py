def meetPoint(line1,line2):
    a,b,e=line1
    c,d,f=line2
    if (a*d)-(b*c)==0: return False
    x=(b*f-e*d)/(a*d-b*c)
    y=(e*c-a*f)/(a*d-b*c)
    return (int(x), int(y)) if x==int(x) and y==int(y) else False

def solution(line):
    points=set()

    for i in range(len(line)):
        for j in range(len(line)):
            if i==j:
                continue
            
            point=meetPoint(line[i],line[j])
            if point: points.add(point)

    x_min = min(point[0] for point in points)
    x_max = max(point[0] for point in points)
    y_min = min(point[1] for point in points)
    y_max = max(point[1] for point in points)

    graph = [["."for j in range(x_max-x_min+1)] for i in range(y_max-y_min+1)]
    for point in points : 
        x,y = point
        graph[y-y_min][x-x_min] = "*"
        
    # 배열과 좌표는 행이 증가하는 방향이 반대이다 -> 위아래를 뒤집어서 제출
    return ["".join(item) for item in graph][::-1]
    

solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])


