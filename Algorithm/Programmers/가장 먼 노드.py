'''
https://school.programmers.co.kr/learn/courses/30/lessons/49189
'''
from collections import defaultdict
import heapq
# 다익스트라 이용
class Test1:
    def solution(n, edge):
        graph=defaultdict(list)
        INF=1e9
        distance=[INF]*(n+1)
        for a,b in edge:
            graph[a].append((b,1))
            graph[b].append((a,1))
        
        def dijkstra(start):
            q=[]
            heapq.heappush(q,(0,start))
            distance[start]=0
            while q:
                dist,now=heapq.heappop(q)
                if dist>distance[now]:
                    continue
                for i in graph[now]:
                    cost=dist+i[1]
                    if cost<distance[i[0]]:
                        distance[i[0]]=cost
                        heapq.heappush(q,(cost,i[0]))
            
        dijkstra(1)
        _max=max(distance[2:])
        return distance[2:].count(_max)
  
# bfs이용
class Test2:
    def bfs(graph,start,distance):
        q=[start]
        visited=set([start])
        while q:
            now=q.pop(0)
            for neighbor in graph[now]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
                    distance[neighbor]=distance[now]+1

    def solution(n, edge):
        graph=defaultdict(list)
        distance=[0]*(n+1)
        for a,b in edge:
            graph[a].append(b)
            graph[b].append(a)
        
        bfs(graph,1,distance)
        _max=max(distance[2:])
        return distance[2:].count(_max)

    solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])