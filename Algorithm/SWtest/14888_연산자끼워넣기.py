"""
https://www.acmicpc.net/problem/14888
3
3 4 5
1 0 1 0
"""
n=int(input())
num=list(map(int,input().split()))
oper_num=list(map(int,input().split()))
_min = [1000000000]
_max = [-1000000000]

operator=list(oper_num[0]*'+'+oper_num[1]*'-'+oper_num[2]*'*'+oper_num[3]*'/')
dep = ['' for _ in range(n - 1)]
visited=[False for _ in range(n)]

def calc(count):
    if count==n-1:
        res=num[0]
        for i in range(len(dep)):
            if dep[i] == '+': 
                res = res + num[i + 1]
            elif dep[i] == '-':
                res = res - num[i + 1]
            elif dep[i] == '*':
                res = res * num[i + 1]
            elif dep[i] == '/':
                res = int(res / num[i + 1])
        if _min[0] > res:
            _min[0] = res
        if _max[0] < res:
            _max[0] = res
        return
            

    for i in range(len(operator)):
        if visited[i]==False:
            visited[i]=True
            dep[count]=operator[i]
            print(dep)
            calc(count+1)
            visited[i]=False

calc(0)
print(_min)
print(_max)