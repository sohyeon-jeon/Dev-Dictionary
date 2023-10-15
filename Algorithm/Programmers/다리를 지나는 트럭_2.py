"""
https://school.programmers.co.kr/learn/courses/30/lessons/42583
"""
from collections import deque

# deque 이용해서 풀기
# sum 함수 대신에 currentWeight 변수를 사용하여 시간을 줄였다.
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    currentWeight = 0

    while bridge_length and truck_weights:
        time += 1
        currentWeight -= bridge.popleft()
        if truck_weights[0] + currentWeight <= weight:
            currentWeight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)

    return time + bridge_length


solution(2, 10, [7, 4, 5, 6])


# list를 이용해서 풀기
# 테스트5번 시간초과 -> sum 함수를 변수로 바꿀 필요가 있다!
def solution1(bridge_length, weight, truck_weights):
    answer = 0

    bridge = [0 for _ in range(bridge_length)]

    while len(bridge) and len(truck_weights):
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if truck_weights[0] + sum(bridge) <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return answer + bridge_length

'''
deque는 연결리스트로 구현이 되어있다.
그래서 삽입,삭제 연산이 많으면 list보다 deque를 사용하는 게 이득이다.
deque 삽입,삭제 -> O(1)
list는 삽입,삭제 -> O(n) 삽입,삭제하려면 해당 위치 이후부터 이동시켜야함.

대신, list는 검색이 빠름!

'''
