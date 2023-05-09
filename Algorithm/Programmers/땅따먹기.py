'''
https://school.programmers.co.kr/learn/courses/30/lessons/12913
'''
#  N : 100,000 이하의 자연수 
# 테스트케이스 개수가 많다. 순열, 백트래킹x 
# dp 
def solution(land):
    # 둘 째 줄부터 각자리숫자에 전에 자기와 열이 겹치지 않는 값 중 최댓값 더하기
    for i in range(1,len(land)):
        land[i][0]+=max(land[i-1][1],land[i-1][2],land[i-1][3])
        land[i][1]+=max(land[i-1][0],land[i-1][2],land[i-1][3])
        land[i][2]+=max(land[i-1][0],land[i-1][1],land[i-1][3])
        land[i][3]+=max(land[i-1][0],land[i-1][1],land[i-1][2])
    return max(land[-1])
solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])