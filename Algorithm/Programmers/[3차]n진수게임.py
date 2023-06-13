'''
https://school.programmers.co.kr/learn/courses/30/lessons/17687
'''

def solution(n, t, m, p):
    result = "0"

    for num in range(1, t * m):
        result += radix_transformation(n, num)
    return result[p-1:t*m:m]

def radix_transformation(base: int, number: int) -> str:
    result = ""

    while number >0:
        number, mod = divmod(number, base)

        # 11진법부터는 변환한 수가 10이상 15이하이면 문자열이다! 
        if base > 10 and (10 <= mod <= 15):
            result += "ABCDEF"[mod % 10]
        else:
            result += str(mod)
    return result[::-1]

# "02468ACE11111111"
solution(16,16,2,1)