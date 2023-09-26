"""
https://school.programmers.co.kr/learn/courses/30/lessons/86971
"""
from collections import defaultdict


def dfs(graph, v, visited, node):
    # 현재 노드를 방문 처리
    visited[v] = True

    node.append(v)
    # 현재 노드와 연결된 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, node)


def solution(n, wires):
    answer = 1e9

    for i in range(len(wires)):
        node = []
        graph = defaultdict(list)

        for u, e in wires[:i] + wires[i + 1 :]:
            graph[u].append(e)
            graph[e].append(u)

        visited = [False] * (n + 1)
        dfs(graph, list(graph.keys())[0], visited, node)
        answer = min(answer, abs(len(node) - (n - len(node))))
    return answer


solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]])

"""
전선 하나씩 끊어보고 dfs로 연결 상태확인
"""
