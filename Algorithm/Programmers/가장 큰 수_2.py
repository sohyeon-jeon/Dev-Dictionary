"""
https://school.programmers.co.kr/learn/courses/30/lessons/42746
"""


def solution(numbers):
    numbers = list(map(str, numbers))
    return str(int("".join(sorted(numbers, key=lambda x: x * 3, reverse=True))))


solution([3, 30, 34, 5, 9])
"""
핵심 아이디어 > 문자열 길이를 3배로 늘린 후에 비교
문자열 비교연산의 경우 문자열 첫번째 인덱스를 아스키숫자로 바꿔서 비교하고 같으면 그 다음 인덱스를 비교한다!
[3, 30, 34, 5, 9]
333
303030
343434
555
999

-> 9 5 34 3 30 
"""
