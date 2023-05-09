'''
https://school.programmers.co.kr/learn/courses/30/lessons/131127
'''
def solution(want, number, discount):
    answer = 0
    shop=[]
    for w,n in zip(want,number):
        shop+=[w]*n
    shop.sort()

    for i in range(len(discount)-len(shop)+1):
        if sorted(discount[i:len(shop)+i])==shop:
            answer+=1
    
    return answer