from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        infol = info[i].split()
        mykey = infol[:-1]
        myval = infol[-1]

        for j in range(5):
            for c in combinations(mykey, j):
                tmp = "".join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(myval))
                else:
                    info_dict[tmp] = [int(myval)]

    for k in info_dict:
        info_dict[k].sort()

    for qu in query:
        myqu = qu.split(" ")
        qu_key = myqu[:-1]
        qu_val = myqu[-1]

        while "and" in qu_key:  # and 제거
            qu_key.remove("and")
        while "-" in qu_key:  # - 제거
            qu_key.remove("-")
        qu_key = "".join(qu_key)  # dict의 key처럼 문자열로 변경

        if qu_key in info_dict:  # query의 key가 info_dict의 key로 존재하면
            scores = info_dict[qu_key]

            if scores:  # score리스트에 값이 존재하면
                enter = bisect_left(scores, int(qu_val))

                answer.append(len(scores) - enter)
        else:
            answer.append(0)

    return answer


# [1,1,1,1,2,4]
solution(
    [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50",
    ],
    [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150",
    ],
)
