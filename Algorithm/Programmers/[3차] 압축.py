'''
https://school.programmers.co.kr/learn/courses/30/lessons/17684
'''
def solution(msg):
    answer = []
    dictionary = {}

    for idx in range(65, 91):
        dictionary[chr(idx)] = idx - 64

    i = 0
    while i < len(msg):
        j = i + 1

        # 사전에 없을 때 까지
        while j < len(msg) + 1 and msg[i:j] in dictionary.keys():
            j += 1
        # 사전에 있는 것
        answer.append(dictionary[msg[i:j - 1]])
        # 사전에 없는 것
        if j < len(msg) + 2:
            dictionary[msg[i:j]] = len(dictionary) + 1

        i = j - 1

    return answer