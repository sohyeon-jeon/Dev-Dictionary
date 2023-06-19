'''
https://school.programmers.co.kr/learn/courses/30/lessons/68936
'''


def solution(arr):
    result=[0,0]
    length=len(arr)
    
    def compression(a,b,l):
        start=arr[a][b]
        for i in range(a,a+l):
            for j in range(b,b+l):
                if arr[i][j]!=start:
                    # 다르면 쪼개서 재귀
                    # (0,0),(2,0),(0,2),(2,2)
                    l=l//2
                    compression(a,b,l)
                    compression(a,b+l,l)
                    compression(a+l,b,l)
                    compression(a+l,b+l,l)
                    return
        # 같으면 그 값 +1 
        result[start]+=1
        
    compression(0,0,length)
    
    print(result)
    return (result)
solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
