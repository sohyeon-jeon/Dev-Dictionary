'''
https://school.programmers.co.kr/learn/courses/30/lessons/147354
'''


def solution(data, col, row_begin, row_end):
    answer = 0
    data=sorted(data,key=lambda x:(x[col-1],-x[0]))
    for i in range(row_begin,row_end+1):
        temp=0
        for item in data[i-1]:
            temp+=item%i
        answer=answer^temp
    return answer