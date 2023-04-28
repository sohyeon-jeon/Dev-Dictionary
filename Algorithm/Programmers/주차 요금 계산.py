'''
https://school.programmers.co.kr/learn/courses/30/lessons/92341
'''
from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    car=dict()
    accumulation=defaultdict(int)
    
    for record in records:
        time,carNum,io=record.split()
        time2val=int(time.split(':')[0])*60+int(time.split(':')[1])
        if io=='IN':
                car[carNum]=time2val
        elif io=='OUT':
            # 테케12 -> 입출차시간이 다른 경우 처리
            if car[carNum]!=time2val:
                accumulation[carNum]+=time2val-car[carNum]
            del car[carNum]

    
    # 출차 내역이 없는 경우 23:59로처리
    if car:
        for key,value in car.items():
            accumulation[key]+=((60*23)+59)-value

    accumulation=dict(sorted(accumulation.items(), key=lambda x:int(x[0])))

    for car_num, time in accumulation.items():
        #기본 시간 보다 작거나 같다면 기본 요금 부과
        if time <= fees[0]:
            accumulation[car_num] = fees[1]
        #기본 시간 보다 오래 이용하였다면
        else:
            accumulation[car_num] = fees[1] + math.ceil((time-fees[0])/fees[2])*fees[-1]
    answer = list(map(lambda x : x[1], sorted(accumulation.items())))
    print(answer)
    return answer
# [14600, 34400, 5000] 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에
solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])