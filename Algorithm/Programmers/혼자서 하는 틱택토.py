from collections import defaultdict
def solution(board):
    bingo=defaultdict(int)
    cnt=defaultdict(int)
    
    for i in range(3):
#         카운트
        cnt["O"]+=board[i].count("O")
        cnt["X"]+=board[i].count("X")
        
#         가로
        if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            bingo[board[i][0]]+=1
#         세로
        if board[0][i]==board[1][i] and board[1][i]==board[2][i]:
            bingo[board[0][i]]+=1
#     대각선1
    if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        bingo[board[1][1]]+=1
#     대각선2
    if board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        bingo[board[1][1]]+=1


# X가 O보다 많거나 / X와 O가 2이상 차이나면
    if cnt["X"]-cnt["O"]>0 or abs(cnt["X"]-cnt["O"])>1:
        return 0
    # O가 이겼을 때 X가 O보다 1개 작은걸 만족하지 않으면 / X가 이겼을 때 O와 X가 같지 않으면 
    # 이상한 게임
    elif (bingo["O"] and cnt["X"]!=cnt["O"]-1) or (bingo["X"] and cnt["O"]!=cnt["X"]):
        return 0
    return 1