'''
https://school.programmers.co.kr/learn/courses/30/lessons/87390
'''
def solution(n, left, right):
    return [max(i//n, i%n)+1 for i in range(left, right+1)]

'''
제한사항 자체가 브루트포스 알고리즘을 사용할 수 없다.
n이 10^7라면, 일일히 내부를 채워서 슬라이싱하는 알고리즘은 턱도 없다.

이런 문제는 규칙성을 확인해야한다.
대각선의 값을 기준으로 왼쪽 직선과 위쪽 직선은 같은 값을 가진다.
위와 아래는 인덱스 값이 약 n만큼 차이가 나고, 대각선의 한 원소로부터 왼쪽 원소들은 인덱스 값이 1씩 줄어든다.

 i // n과 i % n값 중 큰 것을 선택해 1을 더한 값이 인덱스가 된다.
'''