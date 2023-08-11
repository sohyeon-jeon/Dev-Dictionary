"""
https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/
"""


def solution(S):
    stack = []
    for s in S:
        if s in ["(", "{", "["]:
            stack.append(s)
        elif not stack:
            return 0
        elif s == ")" and stack[-1] == "(":
            stack.pop()
        elif s == "}" and stack[-1] == "{":
            stack.pop()
        elif s == "]" and stack[-1] == "[":
            stack.pop()

    if not stack:
        return 1
    else:
        return 0


# 1 or 0

solution("{[()()]}")
