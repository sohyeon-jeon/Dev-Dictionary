"""
https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/
"""


def solution(S):
    stack = []
    for s in S:
        if s in ["(", "{", "["]:
            stack.append(s)
        elif s == ")" and stack[-1] == "(":
            stack.pop()
        elif s == "}" and stack[-1] == "{":
            stack.pop()
        elif s == "]" and stack[-1] == "[":
            stack.pop()
    print(stack)


# 1 or 0

solution("{[()()]}")
