'''
https://school.programmers.co.kr/learn/courses/30/lessons/43164
'''
from collections import defaultdict,deque

def solution(tickets):
        routes=defaultdict(list)
        for a,b in tickets:
            routes[a].append(b)
            routes[a].sort()
            
        stack=['ICN']
        path=[]

        while stack:
            top=stack[-1]
            # 출발 루트에 top이 없거나, 표를 다 써버렸을 때 path에 넣어버리기
            if top not in routes or len(routes[top])==0:
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop(0))
        # 반대로 출력
        return path[::-1]


# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])

class Test1:
    def solution(tickets):

        graph=defaultdict(list)
        for a,b in tickets:
            graph[a].append(b)
            graph[a].sort()
            
        visited=[]
        q=deque(['ICN'])
        visited.append('ICN')
        
        while q and len(graph):
            print(q)
            print(graph)
            p=q.pop()
            
            if graph[p][0]:
                visited.append(graph[p][0])
                q.append(graph[p][0])
                del graph[p][0]

            if len(graph[p])==0:
                del graph[p]
                
        return visited

    '''
    정답은 맞지만 테케1,테케2 실패 -> 
    반례 > [["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]]
    ICN->AAA , ICN->BBB 두 가지 중에 사전순으로 가면 AAA지만 AAA에서 출발하는 길이 없다! 
    '''

