"""'
https://app.codility.com/c/close/trainingCJX2ZJ-J38/?final_task_completed=1
"""


def solution(A, B):
    stack = []
    alive = 0

    for i in range(len(A)):
        if B[i] == 0:
            # 상류로 흐르는 물고기가 하류로 흐르는 물고기 먹음
            while stack and A[i] > stack[-1]:
                stack.pop()
            # 상류로 흐르는 물고기가 하류로 흐르는 물고기 모두 먹음
            if not stack:
                alive += 1
        # 하류로 흐르는 물고기를 stack에 담아준다.
        else:
            stack.append(A[i])
    return len(stack) + alive


solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0])
