"""
https://school.programmers.co.kr/learn/courses/30/lessons/42895
"""
from collections import defaultdict


def calculate(X, Y):
    temp_set = set()

    for x in X:
        for y in Y:
            temp_set.add(x + y)
            temp_set.add(x - y)
            temp_set.add(x * y)
            if y != 0:
                temp_set.add(x // y)
    return temp_set


def solution(N, number):
    answer = -1
    result_dict = defaultdict(list)
    result_dict[1] = {N}
    if number == N:
        return 1

    for n in range(2, 9):
        n_set = set()
        # 숫자로만 되어있는 형태 넣기
        n_set.add(int(str(N) * n))
        # 기존계산결과 재사용
        for i in range(1, n):
            n_set.update(calculate(result_dict[i], result_dict[n - i]))

        if number in n_set:
            answer = n
            break

        result_dict[n] = n_set
    return answer


solution(5, 12)


"""
문제 설명
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.
입출력 예
N	number	return
5	12	4
2	11	3
입출력 예 설명
예제 #1
문제에 나온 예와 같습니다.

예제 #2
11 = 22 / 2와 같이 2를 3번만 사용하여 표현할 수 있습니다.

※ 공지 - 2020년 9월 3일 테스트케이스가 추가되었습니다.
 1번 사용할 때는 그냥 N
# 2번 사용할 때, ex: N=5, 5*5, 5+5, 5-5, 5/5 가 되므로
# 2번일 때는 1번 (op) 1번 : op -> +, -, *, /
# 3번일 때는 1번 (op) 2번, 2번 (op) 1번 ** 반대도 해주어야 빼기와 나누기가 계산됨
# 4번일 때는 1번 (op) 3번, 2번 (op) 2번, 3번 (op) 1번
# N일 때는 1 (op) N-1, 2 (op) N-2, 3 (op) N-3,... N-1 (op) 1 까지 계산해 준다.
# 매번 계산 할 때마다 결과를 set()에 넣어 주어 중복값을 없앤다.
"""
