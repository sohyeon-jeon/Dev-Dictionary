"""
https://school.programmers.co.kr/learn/courses/30/lessons/42883
"""


def solution(number, k):
    stack = []
    for num in number:
        # 스택의 마지막값이 num보다 작으면 계속해서 빼주기 => 큰 수가 앞에 오는게 핵심!
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    return "".join(stack[: len(stack) - k])


solution("4177252841", 4)

"""
O(n)의 시간복잡도 

// 조합은 당연히 시간초과다!
"""
