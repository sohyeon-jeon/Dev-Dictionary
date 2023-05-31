'''
https://school.programmers.co.kr/learn/courses/30/lessons/154539
'''
class Test1:
    def solution(numbers):
        answer = [-1] * len(numbers)
        stack = []

        for idx, number in enumerate(numbers):
            while stack and numbers[stack[-1]] < number:
                answer[stack.pop()] = number

            stack.append(idx)
        return answer

def solution(numbers):
    answer = [-1]*len(numbers)
    for i in range(len(numbers)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if numbers[j] >= numbers[i]:    break
            answer[j] = numbers[i]
    return answer

# [3, 5, 5, -1]
solution([2, 3, 3, 5])