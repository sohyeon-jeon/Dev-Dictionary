'''
https://school.programmers.co.kr/learn/courses/30/lessons/1845
'''
def solution(ls):
    return min(len(ls)/2, len(set(ls)))