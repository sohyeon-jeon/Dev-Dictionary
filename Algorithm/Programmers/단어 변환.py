'''
https://school.programmers.co.kr/learn/courses/30/lessons/43163
'''
import heapq

def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    q=[]
    heapq.heappush(q,(0,begin))
    visited=set([begin])
    while q:
        lv,node=heapq.heappop(q)
        for word in words:
            d=0
            for i in range(len(word)):
                if word[i]!=node[i]:
                    d+=1
            if d==1:
                if word not in visited:
                    visited.add(word)
                    if word==target:
                        return lv+1
                    heapq.heappush(q,(lv+1,word))
                    
    return answer

solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])
'''
우선순위큐를 이용한 dfs
hit -> hot -> dot -> dog -> cog
    -> lot -> log -> log -> cog
hit -> hot -> dot -> lot -> dog -> log -> cog

갈 수 있는 방법이 여러가지다.
heapq를 이용하여 각 층마다 lv 정의해서 최단 경로 구하기
'''