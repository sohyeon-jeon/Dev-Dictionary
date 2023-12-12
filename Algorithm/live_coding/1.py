'''
중첩될 수 있는 인터벌들을 갖는 리스트가 있습니다. 중첩되는 인터벌들을 하나로 합친 새로운 리스트를 반환하세요.

입력 리스트는 정렬되어 있지 않습니다.

예를 들어, [(1, 3), (5, 8), (4, 10), (20, 25)] 가 주어지면, [(1, 3), (4, 10), (20, 25)] 를 반환해야 합니다.
'''
def solution(arr):
    result=[]
    arr.sort()
    for i in range(len(arr)):
        # result가 있고, 그전의 끝점이 현재 원소의 시작점보다 크거나 같으면
        if result and result[-1][1] >= arr[i][0]:
            # 마지막 원소를 중첩되는 인터벌을 합친다!
            # 시작점은 이미 정렬되어 있으므로 그대로 넣고, 끝점은 대소 비교를 한다.
            result[-1]=(result[-1][0],max(arr[i][1],result[-1][1]))
        else:
            result.append(arr[i])
    return result

solution([(1, 3), (5, 8), (4, 10), (20, 25)])
