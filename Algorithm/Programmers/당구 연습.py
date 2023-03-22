'''
https://school.programmers.co.kr/learn/courses/30/lessons/169198               
'''
import math

def solution(m, n, startX, startY, balls):
    answer=[]
    for ball in balls:
        distances=[]
        endX=ball[0]
        endY=ball[1]
        # 3 7 7 7 
        for new_point in [(-startX,startY),(startX,-startY),(2*m-startX,startY),(startX,2*n-startY)]:
            # 대칭점-끝
            p_e_distance=int(math.pow((new_point[0]-endX),2)+math.pow((new_point[1]-endY),2))
            # 대칭점-시작
            p_s_distance=int(math.pow((new_point[0]-startX),2)+math.pow((new_point[1]-startY),2))   
    
            if not (startX==new_point[0]==endX or startY==new_point[1]==endY) or (p_e_distance>p_s_distance):
                distances.append(p_e_distance)
        answer.append(min(distances))
    return answer

solution(10,10,3,7,[[7, 7], [2, 7], [7, 3]])
"""
1. not (startX==new_point[0]==endX or startY==new_point[1]==endY) or (p_e_distance>p_s_distance)
    시작점,대칭점,끝점 x,y가 같다면 쿠션 전에 만날 수 있음-> 제외
2. p_e_distance>p_s_distance
    조건 1을 만족하더라도 쿠션 전에 만나는 상황이 아니므로 정답 후보에 포함
"""
