'''
https://school.programmers.co.kr/learn/courses/30/lessons/17679
'''
def get_black_block(m,n,board):
    blank_block=[]
    for i in range(m):
        for j in range(n):
            if i+1>=m or j+1>=n:
                break
            if board[i][j]==board[i+1][j]==board[i][j+1]==board[i+1][j+1] and board[i][j]!='X':
                blank_block.extend([(i,j),(i+1,j),(i,j+1),(i+1,j+1)])
    blank_block=set(blank_block)
    for x,y in blank_block:
        board[x][y]='X'
    return [board,len(blank_block)]

def down_block(m,n,board):
    # 제일 아래에서 두 번째 행부터 체크! 
    for i in range(m-2,-1,-1):
        for j in range(n):
            k = i
            # 자신 블록 밑에 X가 아닌것이 나올때까지 k값 +1
            while 0 <= k+1 < m and board[k+1][j] == 'X':
                k += 1
            if k != i:
                board[k][j] = board[i][j]
                board[i][j] = 'X'
                
    return board
               
def solution(m, n, board):
    answer = 0
    board=[list(board[i]) for i in range(m)]
    while True:
        board,del_block=get_black_block(m,n,board)

        if del_block==0:
            print(answer)
            return answer
        answer+=del_block
        board=down_block(m,n,board)

# 4
solution(7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"])
