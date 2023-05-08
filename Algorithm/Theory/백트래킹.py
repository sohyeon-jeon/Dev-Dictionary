# 백트래킹은 10 언저리의 숫자까지만 가능(재귀함수를 이용하기 때문에)
# 재귀함수를 이용하는 거면 종료조건 잘 찾기
# 백트래킹 재귀함수 안에서 for 돌면서 숫자 선택(이때 방문 여부 확인)
# 재귀함수에서 m개를 선택할 경우 print
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
rs=[]
chk=[False]*(n+1)

def recur(num):
    if num==m:
        print(' '.join(map(str,rs)))
        return
    for i in range(1,n+1):
        if chk[i]==False:
            chk[i]=True
            rs.append(i)
            recur(num+1)
            rs.pop()
            chk[i]=False

    
recur(0)