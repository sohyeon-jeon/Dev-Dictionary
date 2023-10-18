def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def checkGCD(gcd, array):
    for num in array:
        if num % gcd == 0:
            return 0
    return gcd


def solution(arrayA, arrayB):
    a_gcd = arrayA[0]
    b_gcd = arrayB[0]

    for n in arrayA[1:]:
        a_gcd = gcd(a_gcd, n)

    for n in arrayB[1:]:
        b_gcd = gcd(b_gcd, n)

    return max(checkGCD(b_gcd, arrayA), checkGCD(a_gcd, arrayB))


"""
최대 공약수 구하는 문제
"""
