def solution(H):
    stack = []
    count = 0

    for h in H:
        # 스택이 비어있지 않고, 스택의 맨 위에 있는 높이가 현재 높이보다 큰 경우
        # 스택의 맨 위에 있는 높이를 빼주며 낮은 높이를 제거한다.
        while stack and stack[-1] > h:
            stack.pop()

        # 스택이 비어있거나 스택 맨 위의 높이가 현재 높이보다 작은 경우
        # 새로운 블록이 필요하다
        if not stack or stack[-1] < h:
            count += 1
            stack.append(h)

    return count


solution([8, 8, 5, 7, 9, 8, 7, 4, 8])
"""
N미터가 담겨있는 배열 H를 제공할 때, 최소한의 벽돌 갯수를 return
"""
