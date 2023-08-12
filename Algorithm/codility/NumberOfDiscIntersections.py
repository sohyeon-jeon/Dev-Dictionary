def solution(A):
    arr = []
    for i, v in enumerate(A):
        # -1 시작점 / 1 끝점
        arr.append((i-v, -1))
        arr.append((i+v, 1))

    arr.sort()
    
    intersection = 0
    intervals = 0

    for i,v in enumerate(arr):
        # 닫힐 때에는 열려 있는 원만 하나 닫아준다
        if v[1] == 1 :
            intervals -= 1
        # 새로운 원이 열릴 때에는 기존에 열려있는 원들과 겹치는 부분이 생기므로 총 쌍에서 더해준다.
        if v[1] == -1:
            intersection += intervals
            intervals += 1
    if intersection > 10000000:
        intersection = -1

    return intersection

'''
풀다가 계속 시간초과 나길래 답지 본 문제 ㅠㅠ 
O(n^2)로는 안되고 O(nlogn)이여 되는구나..

'''