import heapq

def solution(N, road, K):
    answer = 0
    INF=int(1e9)
    graph=[[] for _ in range(N+1)]
    distance=[INF]*(N+1)

    # 양방향 연결
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))

    def dijkstra(start):
        q=[]
        heapq.heappush(q,(0,start))
        distance[start]=0
        
        while q:
            dist,now=heapq.heappop(q)
            if distance[now]<dist:
                continue
            for i in graph[now]:
                cost=dist+i[1]
                if cost<distance[i[0]]:
                    distance[i[0]]=cost
                    heapq.heappush(q,(cost,i[0]))

    
    # 1로부터의 거리
    dijkstra(1)
    
    for d in distance:
        if d<=K:
            answer+=1

    return answer

'''
전형적인 다익스트라 문제
(한 지점에서 특정 지점까지의 최단 경로)
'''

solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)