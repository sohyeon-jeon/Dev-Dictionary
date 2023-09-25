"""
https://school.programmers.co.kr/learn/courses/30/lessons/42579
"""
from collections import defaultdict


def solution(genres, plays):
    answer = []
    genresDict = defaultdict(list)
    genresTotal = defaultdict(int)
    for i in range(len(genres)):
        # 실행횟수와 고유번호를 genresDict에 담음
        genresDict[genres[i]].append([plays[i], i])
        # 장르별 실행횟수 더하기
        genresTotal[genres[i]] += plays[i]

    # 장르별 횟수 내림차순 정렬
    genresTotal = dict(sorted(genresTotal.items(), key=lambda x: -x[1]))

    for g in genresTotal.keys():
        # 장르별 / 실행횟수별 내림차순, 고유번호별 오름차순 정렬
        generesSorted = sorted(genresDict[g], key=lambda x: (-x[0], x[1]))

        if len(generesSorted) == 1:
            answer.append(generesSorted[0][1])
        else:
            for i in range(2):
                answer.append(generesSorted[i][1])

    return answer


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
