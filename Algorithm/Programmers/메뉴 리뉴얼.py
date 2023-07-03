'''
https://school.programmers.co.kr/learn/courses/30/lessons/72411/solution_groups?language=python3
'''

from collections import Counter,defaultdict
from itertools import combinations

class Test1:
    def solution(orders, course):
        answer = []
        course_counter=[]
        max_dict=defaultdict(int)

        for num in course:
            max_dict[num]=0

        # 코스요리가 될 수 있는 조합 넣기
        for c in course:
            for order in orders:
                for item in list(combinations(order,c)):
                    course_counter.append(''.join(sorted(item)))
        
        course_counter=dict(Counter(course_counter))

        # 2사람 이상 주문한 조합만 추려서 값 별 최대값 담기
        for key,value in course_counter.items():
            if value>=2:
                max_dict[len(key)]=max(max_dict[len(key)],value)

        # 각 값별 최대값 추리기
        for key,value in course_counter.items():
            for key2,value2 in max_dict.items():
                if len(key)==key2 and value==value2:
                    answer.append(key)
        return sorted(answer)
    
def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)

        # 최빈값 구하는 메소드 사용
        most_ordered = Counter(order_combinations).most_common()
        print(most_ordered)

        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]
   


solution(["XYZ", "XWY", "WXA"],[2,3,4])