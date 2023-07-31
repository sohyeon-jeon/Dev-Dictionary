def solution(n):
    answer = 0
    sum = 0
    k = 1
    while True:
        if k == n + 1:
            break

        for i in range(k, n + 1):
            sum += i
            if sum == n:
                answer += 1
            elif sum > n:
                sum = 0
                break

        k += 1

    print(answer)


solution(15)


# 시간초과
def solution1(n):
    answer = 1
    numbers = [_ for _ in range(1, n + 1)]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if sum(numbers[i:j]) == n:
                answer += 1
                break
    return answer


"""
사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

제한사항
n은 10,000 이하의 자연수 입니다.
입출력 예
n	result
15	4
입출력 예 설명
입출력 예#1
문제의 예시와 같습니다.

dp
1 3 6 10 15
4 9 15
7 15
15  



"""
