'''
https://school.programmers.co.kr/learn/courses/30/lessons/49191
'''

'''
처음에 선후관계때문에 위상정렬로 풀려고했는데 위상정렬 조건에 사이클이 있으면 안되었다.
그래서 다른 블로그를 참고해서 플루이드워셜을 이용했다.

여기서 가장 중요한 명제는,
승패가 결정이 나지 않았을 때
- a가 k를 이기고 k가 b를 이기면 -> a는 b를 이긴다
- a가 k에게 지고 k가 b에게 지면 -> a는 b에게 진다.
이다.
'''

class Test1:
    def solution(n, results):
        answer = 0
        graph=[[0]*(n+1) for _ in range(n+1)]
                
        for a,b in results:
            # 이기면 1, 지면 -1
            graph[a][b]=1
            graph[b][a]=-1
        
        for k in range(1,n+1):
            for a in range(1,n+1):
                for b in range(1,n+1):
                    # 자기자신이 아니면서 아직 승패가 결정이 안난 경우
                    if a!=b and graph[a][b]==0:
                        # a가 k를 이기고 k가 b를 이기면 -> a는 b를 이긴다
                        if graph[a][k]==1 and graph[k][b]==1:
                            graph[a][b]=1
                        # a가 k에게 지고 k가 b에게 지면 -> a는 b에게 진다.
                        elif graph[a][k]==-1 and graph[k][b]==-1:
                            graph[a][b]=-1

        # 자기 자신을 제외하고 승패가 결정났으면 확실
        for i in range(1,n+1):
            if graph[i][1:].count(0)==1:
                answer+=1
                    
        return answer

from collections import defaultdict
class Test2:
    
    def solution(n, results):
        answer = 0
        win, lose = defaultdict(set), defaultdict(set)
        for result in results:
                lose[result[1]].add(result[0])
                win[result[0]].add(result[1])

        for i in range(1, n + 1):
            for winner in lose[i]: win[winner].update(win[i])
            for loser in win[i]: lose[loser].update(lose[i])

        print(win,lose)

        for i in range(1, n+1):
            if len(win[i]) + len(lose[i]) == n - 1: answer += 1
        return answer


    solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])

