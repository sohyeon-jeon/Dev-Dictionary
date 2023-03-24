### 순차탐색
리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
``` python
def sequential_search(n,target,array):
    for i in range(n):
        if array[i]==target:
            return i+1

print('생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요')    
input_data=input().split()
n=int(input_data[0])
target=input_data[1] 

print('앞서 적은 원소 개수만큼 문자열을 입력하세요')
array=input().split()

print(sequential_search(n,target,array))
```
- 데이터 정렬 여부와 상관없이 앞에 있는 원소부터 하나씩 확인해야한다.
- 데이터의 개수가 n일때, 최악의 경우 O(n)의 시간복잡도를 가진다.

### 이진탐색
- 내부의 데이터가 이미 정렬되어 있어야 한다.
- 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교한다.
- 한 번 확인할 때마다 확인하는 원소가 절반씩 줄어들어 시간복잡도가 O(logn)이다.
- 탐색 범위가 1,000만을 넘어가면 이진 탐색을 사용해보자! 
``` python
# 재귀함수 이진 탐색
def binary_search(array,target,start,end):
    if start>end:
        return None
    mid=(start+end) // 2
    if array[mid]==target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array,target,mid+1,end)

# 원소의 개수n, 찾고자 하는 문자열 target 
n,target=list(map(int,input().split()))
# 전체 원소 입력받기
array=list(map(int,input().split()))

# 이진 탐색 수행 결과 출력
result=binary_search(array,target,0,n-1)
if result==None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)

"""
입력 > 
10 7
1 3 5 7 9 11 13 15 17 19
출력 > 
4
"""
```

```python
# 반복문을 통한 이진 탐색
def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

# 원소의 개수n, 찾고자 하는 문자열 target 
n,target=list(map(int,input().split()))
# 전체 원소 입력받기
array=list(map(int,input().split()))

# 이진 탐색 수행 결과 출력
result=binary_search(array,target,0,n-1)
if result==None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)
"""
입력 > 
10 7
1 3 5 7 9 11 13 15 17 19
출력 > 
4
"""
```
즉, 이진 탐색은 재귀함수와 반복문을 이용해 구현할 수 있다.

### 이진 탐색 트리
- 부모 노드보다 왼쪽 자식 노드가 작다.
- 부모 노드보다 오른쪽 자식 노드가 크다.
- 즉, **왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드**


