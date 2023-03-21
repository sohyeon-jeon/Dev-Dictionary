'''
                        
'''
import math
class Test1:
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
    '''
    직선을 한 번 만나는 두 점 사이의 최소거리는 한 점을 해당 직선에 대칭한 대칭점과 다른 한 점 사이의 거리와 같다.
    단,
    1. 시작점,대칭점,끝점의 x,y가 모두 같지 않은 경우
    2. (대칭점-끝점)거리>(대칭점-시작점)거리인 경우
    '''
        
                   

        



        
solution(10,10,3,7,[[7, 7], [2, 7], [7, 3]])
