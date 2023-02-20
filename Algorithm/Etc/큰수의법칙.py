"""
source : 2019 국가 교육기관 코딩테스트

다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙.
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과할 수 없다.
입력>
5 8 3
2 4 5 4 6
출력>
46
"""
def test1():
    n,m,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    result=0

    first=arr[0]
    second=arr[1]

    while True:
        #가장 큰 수 k번 만큼 더하기
        for _ in range(k):
            if m==0:
                break
            result+=first
            m-=1
        # 두 번째로 큰 수 한 번 더하기
        if m==0:
            break
        result+=second
        m-=1
    print(result)

def test2():   
    n,m,k=map(int,input().split())
    arr=list(map(int,input().split()))

    arr.sort()
    first=arr[n-1]
    second=arr[n-2]

    # [6,6,6,5],[6,6,6,5] 반복되는 수열 파악
    # 큰 수가 반복되는 횟수 count, 나머지 찾기 
    count=int(m/(k+1))
    rest=m%(k+1)

    result=0
    result+=(first*count*k)+(second*count)
    result+=first*rest
    print(result)




