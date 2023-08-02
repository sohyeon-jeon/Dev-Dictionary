# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, Y, D):
    cnt, mod = divmod((Y - X), D)
    if mod > 0:
        cnt += 1
    return cnt


solution(10, 70, 30)
