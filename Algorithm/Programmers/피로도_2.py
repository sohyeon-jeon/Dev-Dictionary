"""
https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""
from itertools import permutations


def solution(k, dungeons):
    answer = []
    # 순열: 순서 고려, 중복 허용x
    for p in permutations(dungeons, len(dungeons)):
        # 유저가 탐험할 수 있는 던전 수
        energy = k
        cnt = 0
        for r in p:
            # 최소 필요 피료도가 현재 체력 이상이면
            if energy >= r[0]:
                # 던전 탐험 ㄱ~
                energy -= r[1]
                cnt += 1
        answer.append(cnt)
    return max(answer)


solution(80, [[80, 20], [50, 40], [30, 10]])
