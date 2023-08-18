# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # 1~6까지의 배열을 추가
    N = len(A)
    answer = [A[0]] * (N + 6)

    # 6의 범위안에서 최댓값 구하기
    for i in range(1, len(A)):
        answer[i + 6] = A[i] + max(answer[i : i + 6])
    return answer[-1]


# 1+9-2=8 리턴
solution([1, -2, 0, 9, -1, -2])
