'''
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
'''
from collections import defaultdict

def min_reorder(n, connections):
    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append((b, 1))
        graph[b].append((a, 0))

    visited = set()
    changes = 0
    stack = [0]

    while stack:
        node = stack.pop()
        visited.add(node)
        for neighbor, direction in graph[node]:
            if neighbor not in visited:
                changes += direction
                stack.append(neighbor)

    print(changes)
    return changes

min_reorder(6,[[0,1],[1,3],[2,3],[4,0],[4,5]])

"""
이 코드는 입력으로 도시의 수 n과 도로의 연결 정보 connections를 받아, 각 도시가 0번 도시에 방문할 수 있도록 도로의 방향을 바꾸는 최소한의 도로 개수를 반환합니다.

우선 defaultdict(list)를 사용해 인접 리스트 그래프를 생성합니다. for 루프를 돌며 connections에 있는 모든 도로에 대해 출발 도시 a와 도착 도시 b를 인접 리스트 그래프에 추가합니다. 이때 a에서 b로 가는 방향은 1, b에서 a로 가는 방향은 0으로 표시합니다.

다음으로 방문한 노드를 저장할 visited 집합, 방향을 바꾼 도로 개수를 저장할 changes 변수, DFS 탐색을 위한 스택 stack을 생성합니다. 스택의 초기 값으로 0번 도시를 추가합니다.

스택이 빌 때까지 다음의 작업을 반복합니다. 스택에서 노드를 꺼내서 방문 처리하고, 해당 노드의 모든 이웃 노드를 방문하지 않았다면 방향을 바꾼 도로 개수 changes에 더하고 이웃 노드를 스택에 추가합니다.

마지막으로 changes 변수를 반환합니다.
"""