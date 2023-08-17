# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if not A or len(A) < 2:
        return 0
    max_profit = 0
    min_price = A[0]
    for price in A:
        max_profit=max(max_profit,price-min_price)
        min_price=min(min_price,price)
    return max_profit