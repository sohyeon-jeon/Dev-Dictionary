'''
https://school.programmers.co.kr/learn/courses/30/lessons/42628#
'''
import heapq

# 최소힙으로 구현하고 nlargest을 사용해서 최대값 뽑기
def solution(operations):
    q=[]
    for operation in operations:
        cmd,num=operation.split()
        if cmd=="I":
            heapq.heappush(q,int(num))
        elif cmd=="D":
            if len(q)>0:
                if num=="1":
                    q=heapq.nlargest(len(q),q)[1:]
                    heapq.heapify(q)
                elif num=="-1":
                    heapq.heappop(q)

    if len(q)>0:
        return [heapq.nlargest(len(q),q)[0],q[0]]
    else:
        return [0,0]


# 최대힙과 최소힙 각각 만듬
def solution1(operations):
    heap=[]
    max_heap=[]
    
    for operation in operations:
        cmd,num=operation.split()
        if cmd=="I":
            num=int(num)
            heapq.heappush(heap,num)
            heapq.heappush(max_heap,(num*-1,num))
            
        elif cmd=="D":
            if heap:
                if num=="1":
                    max_value=heapq.heappop(max_heap)[1]
                    heap.remove(max_value)
                elif num=="-1":
                    min_value=heapq.heappop(heap)
                    max_heap.remove((min_value*-1,min_value))

    if heap:
        return [heapq.heappop(max_heap)[1],heapq.heappop(heap)]
    else:
        return [0,0]

                

                