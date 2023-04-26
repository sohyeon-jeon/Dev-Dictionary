'''
https://school.programmers.co.kr/learn/courses/30/lessons/81302
# '''

def chkDistance(place):
    person=[(i,j) for i in range(5) for j in range(5) if place[i][j]=='P']
    '''
    * 거리두기 안되는 경우
    1. 두 점 사이의 거리 1
    2. 거리 2, 행이 같고, 두 점 사이에 파티션(X) 없음
    3. 거리 2, 열이 같고, 두 점 사이에 파티션(X) 없음
    4. 거리 2, 행/열 다르고, 파티션이 하나라도 없는 경우
    '''
    for r1,c1 in person:
        for r2,c2 in person:
            distance=abs(r1-r2)+abs(c1-c2)
            if distance==1:
                return 0
            elif distance==2:
                if r1==r2 and place[r1][(c1+c2)//2]!='X':
                    return 0
                elif c1==c2 and place[(r1+r2)//2][c1]!='X':
                    return 0
                # 대각선 관계
                elif r1!=r2 and c1!=c2:
                    if place[r1][c2]!='X' or place[r2][c1]!='X':
                        return 0
    return 1
                    
def solution(places):
    answer = []
    # 각 place들을 check_distance함수로 조사
    for place in places:
        answer.append(chkDistance(place))        
    return answer



# [1, 0, 1, 1, 1]
solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
