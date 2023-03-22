'''
https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3
'''
def dfs(v,visited,computers):
    visited[v]=True
    for i in range(len(computers)):
        if computers[v][i]==1 and visited[i]==False:
            dfs(i,visited,computers)
         
def solution(n, computers):
    answer=0
    visited=[False]*n
    for i in range(n):
        if not visited[i]:
            dfs(i,visited,computers)
            answer+=1
    return answer

solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])