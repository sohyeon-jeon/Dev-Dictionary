'''
https://school.programmers.co.kr/learn/courses/30/lessons/131701
'''
def solution1(elements):
    cycle=elements*2
    dp=[0]*len(elements)
    sum_list=list()

    for i in range(len(elements)):
        for j in range(len(elements)):
            dp[j]+=cycle[j+i]
        sum_list.extend(dp)

    return len(set(sum_list))

def solution2(elements):
    n=len(elements)
    elements*=2
    sum_set=set(elements)

    for sub_len in range(2, n + 1):
        for i in range(n):
            sum_set.add(sum(elements[i:i+sub_len]))
    return len(sum_set)

solution1([7,9,1,1,4])

'''
위 아래 모두 시간복잡도 O(n^3)
'''

