"""
https://school.programmers.co.kr/learn/courses/30/lessons/49189
"""
import heapq
from collections import defaultdict


# 다익스트라 이용
def solution1(n, edge):
    graph = [[] for _ in range(n + 1)]
    distance = [1e9] * (n + 1)

    for a, b in edge:
        # (연결노드,거리)
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    # 다익스트라 이용
    # 다익스트라 : 특정 노드에서 다른 여러개의 노드 사이의 최단거리를 구할 때 유용
    q = []
    start = 1
    # (거리,시작노드)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    max_value = max(distance[1:])
    return distance[1:].count(max_value)


def bfs(graph, start, distance):
    q = [start]
    visited = set([start])
    while q:
        now = q.pop(0)
        for neighbor in graph[now]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                distance[neighbor] = distance[now] + 1


def solution(n, edge):
    graph = defaultdict(list)
    distance = [0] * (n + 1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    bfs(graph, 1, distance)
    _max = max(distance[2:])
    return distance[2:].count(_max)


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
"""
n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

제한사항
노드의 개수 n은 2 이상 20,000 이하입니다.
간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
입출력 예
n	vertex	return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3
입출력 예 설명
예제의 그래프를 표현하면 아래 그림과 같고, 1번 노드에서 가장 멀리 떨어진 노드는 4,5,6번 노드입니다.
"""
