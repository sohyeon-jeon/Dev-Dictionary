'''
문제
철수는 온라인으로 컴퓨터공학강의를 듣고 있다.

이때 각 온라인강의는 선수강의가 있을 수 있는데, 선수 강의가 있는 강의는 선수 강의를 먼저. 들어야만 해당강의를 들을 수 있다.

예를들어 '알고리즘’ 강의의 선수 강의로 '자료구조'가 존재한다면, ‘자료구조를 들은 이후에 ‘알고리즘' 강의를 들을 수 있다.

철수는 총 N개의 강의를 듣고자 한다. 모든 강의는 1번부터 N번까지의 번호를 가진다.

또한 동시에 여러 개의 강의를 들을 수 있다고 가정한다.

예를 들어 N=3일 때, 3번강의의 선수 강의로 1번과 2번강의가 있고, 1번과 2번강의는 선수강의가 없다고 가정하자.

그리고 각 강의에 대하여 강의 시간이 다음과 같다고 가정하자.

 

1번 강의: 30시간

2번 강의: 20시간

3번 강의: 40시간


 

이 경우 1번 강의를 수강하기까지의 최소 시간은 30시간, 2번 강의를 수강하기까지의 최소 시간은 20시간, 3번 강의를 수강하기까지의 최소 시간은 70시간이다.

철수가 듣고자 하는 N개의 강의 정보가 주어졌을 때, N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력하는 프로그램을 작성하시오.

 

입력 조건
첫째줄에 철수가 듣고자 하는 강의의 수 N(1≤N≤500)이 주어진다.

다음 N개의 줄에는 각 강의의 강의 시간과 그. 강의를 듣기 위해 먼저 들어야하는 강의들의 번호가 자연수로 주어지며, 각. 자연수는 공백으로 구분한다. 이때 강의시간은 100,000이하의 자연수이다 .각 강의번호는 1부터 N까지로 구성되며. 각줄은 -1로 끝난다.

 

출력 조건
N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력한다

 

입력 예시
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
 

출력 예시
10
20
14
18
17
'''
from collections import deque
import copy

v=int(input())
indegree=[0]*(v+1)
graph=[[] for i in range(v+1)]
time=[0]*(v+1)

for i in range(1,v+1):
    data=list(map(int,input().split()))
    # 첫 번째 수는 시간 정보를 담고 있음
    time[i]=data[0]
    for x in data[1:-1]:
        indegree[i]+=1
        graph[x].append(i)

def topology_sort():
    result=copy.deepcopy(time)
    q=deque()

    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
        
    while q:
        now=q.popleft()
        for i in graph[now]:
            result[i]=max(result[i],result[now]+time[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

        for i in range(1,v+1):
            print(result[i])

topology_sort()