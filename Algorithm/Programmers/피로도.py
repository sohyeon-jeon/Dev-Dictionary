from itertools import permutations

class Test1:
    def solution(k, dungeons):
        answer = []
        # 가능한 순열 미리 만들어 두기
        routes=list(permutations(dungeons,len(dungeons)))
        
        for route in routes:
            energy=k
            count=0
            for r in route:
                if energy>=r[0]:
                    energy-=r[1]
                    count+=1
                else:
                    break
            answer.append(count)       
        return max(answer)

'''
dfs 이용
visited 설정 해주고 dfs 부른 다음 다시 visited[j] = 0으로 해서 모든 경우를 따지도록 계산했다.
'''
answer = 0
N = 0
visited = []
def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt
    
    
    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            print(visited)
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
 
solution(80,[[80,20],[50,40],[30,10]])