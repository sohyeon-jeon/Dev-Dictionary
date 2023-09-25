"""
https://school.programmers.co.kr/learn/courses/30/lessons/42584
"""


# 통과했지만 시간은 느리당!
def solution1(prices):
    answer = []
    for i in range(len(prices)):
        # 끝까지 가격이 안떨어지는 경우
        time = len(prices) - i - 1

        for j in range(i + 1, len(prices)):
            # 주식이 떨어지는 경우
            if prices[i] > prices[j]:
                time = j - i
                break
        answer.append(time)
    return answer


# 스택 이용
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])

    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer


solution([1, 2, 3, 2, 3])


"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.
입출력 예
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
※ 공지 - 2019년 2월 28일 지문이 리뉴얼되었습니다.

1 2 3 
4 3 1 1 0 
"""
