def solution(board):
    answer = 1 if 1 in board[0] or 1 in board[-1] else 0
    for m in range(1, len(board)):
        for n in range(1, len(board[0])):
            if board[m][n] == 1:
                board[m][n] = (
                    min(board[m - 1][n], board[m - 1][n - 1], board[m][n - 1]) + 1
                )
                answer = max(answer, board[m][n])

    return answer**2


solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]])
"""
dp문제
"""
