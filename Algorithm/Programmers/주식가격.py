"""
https://school.programmers.co.kr/learn/courses/30/lessons/42584
"""


# 통과했지만 시간은 느리당!
def solution1(prices):
    answer = []
    for i in range(len(prices)):
        # 끝까지 가격이 안떨어지는 경우
        time = len(prices) - i - 1

        for j in range(i + 1, len(prices)):
            # 주식이 떨어지는 경우
            if prices[i] > prices[j]:
                time = j - i
                break
        answer.append(time)

    return answer


def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        if stack:
            while stack and stack[-1][1] > prices[i]:
                j, _ = stack.pop()
                answer[j] = i - j
        stack.append([i, prices[i]])

    for s in stack:
        answer[s[0]] = len(prices) - s[0] - 1
    return answer


solution([1, 2, 3, 1, 3])
