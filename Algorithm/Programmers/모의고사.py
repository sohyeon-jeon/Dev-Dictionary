'''
https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3
'''
from collections import defaultdict
def solution(answers):
    answer = []
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    
    correct=defaultdict(int)

    
    for i,v in enumerate(answers):
        if answers[i]==one[i%len(one)]:
            correct[1]+=1
        if answers[i]==two[i%len(two)]:
            correct[2]+=1
        if answers[i]==three[i%len(three)]:
            correct[3]+=1
            
    max_score=max(correct.values())
    for k,v in correct.items():
        if v==max_score:
            answer.append(k)
    
    return sorted(answer)