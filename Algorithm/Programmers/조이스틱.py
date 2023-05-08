'''
https://school.programmers.co.kr/learn/courses/30/lessons/42860#
'''
def solution(name):
    answer = 0
    min_move=len(name)-1
    for i,char in enumerate(name):
        answer+=min(ord(char)-ord('A'),ord('Z')-ord(char)+1)
        # 해당 알파벳 다음부터 연속된 a 문자열 찾기
        next=i+1
        while next<len(name) and name[next]=='A':
            next+=1
        # 기존, 연속된 a의 왼쪽시작, 연속된 a의 오른쪽 시작 갱신
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
    answer+=min_move
    print(answer)
    return answer

solution('BBBBAAAABA')

'''
연속되는 A가 있을 때, 그것의 왼쪽이나 오른쪽부터 시작하여 알파벳을 변경하는 것이 가장 효율적이다.
연속되는 A가 있는 곳에는 굳이 갈 필요가 없다 -> 그 부분을 제외하고 수정
연속되는 A가 여러군데인 경우 긴 부분을 안 가는게 제일 효율적이다.
'''


class fail:
    import math

    def solution(name):
        answer = 0
        indexes = [i for i, c in enumerate(name) if c != 'A' and i!=0]
        if indexes:
            move=min(indexes[-1],len(name)-indexes[0],len(name)-1)
        else:
            return 0
        for n in name:
    #         위쪽 방향키 이동
            if ord(n)-ord('A')<=13:
                answer+=ord(n)-ord('A')
    #             아래쪽으로 이동
            elif ord(n)-ord('A')>13:
                answer+=26-(ord(n)-ord('A'))
        answer+=move

        return answer
    '''
    테케 실패
    '''                                                         