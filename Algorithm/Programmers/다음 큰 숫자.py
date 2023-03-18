def solution(n):
    next=n
    while True:
        next+=1
        if bin(n).count('1')==bin(next).count('1'):
            return next
solution(78)