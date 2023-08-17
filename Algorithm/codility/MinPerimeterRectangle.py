def solution(N):
    min_perimeter = float('inf')
    i = 1
    
    # N의 약수는 N의 제곱근보다 작거나 같다, 범위 조절해서 시간 줄이자..
    while i * i <= N:
        if N % i == 0:
            factor = N // i
            perimeter = 2 * (i + factor)
            min_perimeter = min(min_perimeter, perimeter)
        i += 1
    
    return min_perimeter