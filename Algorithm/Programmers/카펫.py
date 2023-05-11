def solution(brown, yellow):
    w=1
    while True:
#         가로>=세로
        if yellow%w==0 and w>=(yellow//w):
            h=yellow//w
#             갈색 가로=(노란색 가로+2), 갈색 세로=(노란색 세로+2)
            if ((w+h+4)*2)-4==brown:
                return [w+2,h+2]
        w+=1
