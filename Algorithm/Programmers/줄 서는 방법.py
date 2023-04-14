from itertools import permutations

class Test1:
    def solution(n, k):
        arr=[i for i in range(1,n+1)]
        result=sorted(list(permutations(arr,n)))
        return list(result[k-1])

    solution(3,5)

'''
순열: 순서고려하여 나열, ex> 5개의 서로 다른 공 중에서 3개를 골라서 나열한다., 조합 : 순서고려x, 4개의 공 중에서 무작위로 2개 공을 고른다.
'''
'''
순열로 풀면 시간 초과가 발생한다.
나머지 순열의 요소는 계산될 필요가 없다.
수학적계산을 통해 계산한다.
'''
import math

def solution(n,k):
    k-=1
    answer=[]
    numbers=list(range(1,n+1))

    for i in range(n, 0, -1):
        div, k = divmod(k, math.factorial(i-1))
        answer.append(numbers.pop(div))
        
    return answer

solution(3,5)