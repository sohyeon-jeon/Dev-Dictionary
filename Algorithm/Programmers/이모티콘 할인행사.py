'''
https://school.programmers.co.kr/learn/courses/30/lessons/150368
'''
from itertools import product

class Test1:
    def solution(users, emoticons):
        answer=[]
        # 이모티콘 갯수만큼 할인율 [40,30,20,10]의 중복순열을 구함
        discounts = product([40,30,20,10],repeat=len(emoticons))
        for discount in discounts:
            # 이모티콘 플러스 서비스 가입자, 이모티콘 판매액
            subscribers=0
            total_cost=0
            for user in users:
                # 각 사용자마다의 이모티콘 구입 비용
                user_cost=0
                for i in range(len(emoticons)):
                    # 이모티콘 할인율이 자신이 허용한 할인율 이상이면 이모티콘 구입
                    if discount[i]>=user[0]:
                        user_cost+=emoticons[i]*(100-discount[i])//100
                # 이모티콘 구입 비용이 자신의 기준에 따라 이모티콘 구매 비용의 합보다 크면 
                # 이모티콘 플러스 서비스 구독
                # 아니면 이모티콘 판매액에 누적
                if user_cost>=user[1]:
                    subscribers+=1
                else:
                    total_cost+=user_cost

            answer.append([subscribers,total_cost])
        # 구독자를 기준으로 내림차순, 이모티콘 판매액을 기준으로 내림차순해서 제일 첫 번째 값!
        '''
        1. 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
        2. 이모티콘 판매액을 최대한 늘리는 것.
        1번 목표가 우선이며, 2번 목표가 그 다음입니다.
        '''
        return sorted(answer,key=lambda x:(-x[0],-x[1]))[0]
            
    solution([[40, 10000], [25, 10000]],[7000, 9000])

    '''
    users 최대 100, emoticons 최대 7, 할인율은 [10,20,30,40] 4종류

    [10,20,30,40] 4종류의 할인율로 최대 7가지의 이모티콘 중복순열을 구해보면,
    product([10,20,30,40],repeat=7 -> 약 16000
    총 100*7*16000=1100만번 수행 -> 1억번을 넘지 않는다
    -> 브루트포스로 가능하다.
    '''
class Test2:
    def solution(users, emoticons):
        answer=[0,0]
        discounts = product([40,30,20,10],repeat=len(emoticons))
        for discount in discounts:
            subscribers=0
            total_cost=0
            for user in users:
                user_cost=0
                for i in range(len(emoticons)):
                    if discount[i]>=user[0]:
                        user_cost+=emoticons[i]*(100-discount[i])//100
                if user_cost>=user[1]:
                    subscribers+=1
                else:
                    total_cost+=user_cost
            # 리스트끼리도 max 함수를 쓸 수도 있다!
            answer=max(answer,[subscribers,total_cost])
        return answer
    solution([[40, 10000], [25, 10000]],[7000, 9000])

           



