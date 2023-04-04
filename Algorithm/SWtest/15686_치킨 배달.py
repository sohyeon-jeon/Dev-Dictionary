"""
https://www.acmicpc.net/problem/15686
"""

def combinations(array,r):
    for i in range(len(array)):
        if r==1:
            yield [array[i]]
        else:
            for next in combinations(array[i+1:],r-1):
                yield [array[i]]+next


n,m=map(int,input().split())
chicken,house=[],[]

for r in range(n):
    data=list(map(int,input().split()))
    for c in range(n):
        if data[c]==1:
            house.append((r,c))
        elif data[c]==2:
            chicken.append((r,c))


candidates=list(combinations(chicken,m))

def get_sum(candidate):
    result=0
    for hx,hy in house:
        temp=1e9
        for cx,cy in candidate:
            temp=min(temp,abs(hx-cx)+abs(hy-cy))
        result+=temp
    return result

# 도시의 치킨 거리 중 최소값을 구한다.
result=1e9
for candidate in candidates:
    result=min(result,get_sum(candidate))
print(result)
