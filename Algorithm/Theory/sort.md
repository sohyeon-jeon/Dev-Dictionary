### 선택 정렬
- 이중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾼다.
- 가장 작은 것을 선택
``` python
import time
start=time.time()
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i],array[min_index]=array[min_index],array[i] 
print(array)
end=time.time()
print(end-start)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 5.1021575927734375e-05
```
- **선택 정렬**은 데이터를 앞으로 보내는 과정을 N-1번 반복하면 정렬이 완료된다.
- 시간복잡도 : O(n^2)

### 삽입 정렬
- 데이터를 적절한 위치에 '삽입'한다.
- 두 번째 데이터부터 시작한다. 그 자체로 정렬되어 있다고 판단한다.
``` python
import time
start=time.time()
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j]<array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j],array[j-1]=array[j-1],array[j]
        else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)
end=time.time()
print(end-start)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 5.459785461425781e-05
```
**삽입정렬**의 시간복잡도: O(n^2)  
삽입 정렬의 리스트가 거의 정렬되어 있는 상태라면 최선의 경우는 O(n)의 시간복잡도를 가진다.

### 퀵 정렬
기준 데이터(피벗)를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
- 리스트에서 첫 번째 데이터를 피벗으로 정한다. 
- 첫 번째 원소(5)를 피벗으로 설정했으면 왼쪽은 5보다 큰 데이터, 오른쪽에서는 5보다 작은 데이터를 선택한다.   
```
5(p)790316248  
5(p)7(선택)9031624(선택)8  
5(p)490316278 -> 변경  
5(p)49(선택)03162(선택)78  
5(p)420316978 -> 변경
5(p)42031(선택)6(선택)978 -> 왼쪽으로부터 찾는 값과 오른쪽으로부터 찾는 값이 엇갈림 -> 작은데이터와 피벗의 위치를 바꾼다.
142035(p)6978 -> 피벗(5)기준으로 왼쪽은 5보다 작고 오른쪽은 5보다 크다.
...
이후 왼쪽,오른쪽 각각에서 피벗을 설정하여 동일한 방식으로 정렬을 수행한다.
```
``` python
import time
start=time.time()
array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start>=end:
        return
    pivot=start # 피벗은 첫 번째 원소
    left=start+1
    right=end
    while left<=right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left<=end and array[left]<=array[pivot]:
            left+=1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right>start and array[right]>=array[pivot]:
            right-=1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left>right:
            array[right],array[pivot]=array[pivot],array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[left],array[right]=array[right],array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)
end=time.time()
print(end-start)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 4.553794860839844e-05
```

``` python
import time

array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array)<=1:
        return array

    pivot=array[0] # 피벗은 첫 번째 원소
    tail=array[1:] # 피벗을 제외한 리스트

    left_side=[x for x in tail if x<=pivot]
    right_side=[x for x in tail if x>pivot]

    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))
```
**파이썬의 장점을 살린 퀵 정렬 소스코드**
- 매우 직관적이다.
- 시간은 일반 퀵 정렬보다 오래 걸릴 수 있다.

- 퀵 정렬의 평균 시간 복잡도 : O(nlogn)
- 최악의 경우에는 시간 복잡도가 O(n^2)가 될 수 있다.
- 삽입 정렬은 이미 정렬되어 있으면 매우 빠르게 동작하는데, 퀵 정렬은 이미 정렬되어 있는 경우라면 느리게 동작한다.

### 계수 정렬 
- 특정한 조건이 부합할 떄만 사용할 수 있지만 매우 빠른 정렬 알고리즘
- 데이터 개수가 n, 데이터 중 최대값이 k일때 계수정렬은 최악의 경우에도 O(n+k)를 보장한다. 매우 빠르다.
- 데이터 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용, 중복된 데이터 개수가 많을 때 사용
- 가장 큰 데이터와 가장 작은 데이터 차이가 1,000,000을 넘지 않을 때 효과적으로 사용
``` python
array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언
count=[0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]]+=1 # 각 데이터에 해당하는 인덱스 값 증가

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')
# 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9 
```

### 정렬 라이브러리
파이썬의 정렬 라이브러리는 병합 정렬 기반이다.
퀵 정렬보다는 느리지만 최악의 경우에도 O(nlogn)을 보장한다





