'''
https://school.programmers.co.kr/learn/courses/30/lessons/42626
'''

import heapq
def solution(scoville, K):
    answer = 0
#     heapq = 우선순위 큐, 최소힙/최대힙 구현
    heapq.heapify(scoville)
    while scoville[0]<K:
        mix=heapq.heappop(scoville)+(heapq.heappop(scoville)*2)
        heapq.heappush(scoville,mix)
        answer+=1
        if len(scoville)==1 and scoville[0]<K:
            return -1
    return answer