"""
https://school.programmers.co.kr/learn/courses/30/lessons/134239
"""
def solution(k, ranges):
    answer = []
    area = [0]

    i = 0
    prev_k = k

    while k > 0:
        if k == 1:
            break

        if k % 2 == 0:
            k = k // 2
        else:
            k = (k * 3) + 1
        i += 1

        area.append(((prev_k + k) * 1) / 2)
        prev_k = k


    # 누적합 넓이
    for i in range(1, len(area)):
        area[i] += area[i - 1]


    for r in ranges:
        s, e = r[0], len(area) - 1 + r[1]

        if s > e:
            answer.append(-1.0)
        else:
            answer.append(area[e] - area[s])

    return answer


solution(3, [[0, 0], [1, -2], [3, -3]])
'''
문제 이해하는 데 오래걸린 문제ㅠ

콜라츠 추측 하는 동안 그 구간에서의 넓이(사다리꼴 넓이)를 구함
그리고 전체 누적합 넓이 구하기
구간마다 빼주면 됨
'''