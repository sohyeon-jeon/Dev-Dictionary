"""
https://school.programmers.co.kr/learn/courses/30/lessons/176962#
"""


def solution(plans):
    answer = []
    stack = []
    for i in range(len(plans)):
        t, m = map(int, plans[i][1].split(":"))
        plans[i][1] = t * 60 + m
        plans[i][2] = int(plans[i][2])

    plans = sorted(plans, key=lambda x: x[1])
    print(plans)

    for i in range(len(plans) - 1):
        # 다음 과제까지 남은 시간이 내 과제 수행시간보다 남으면 -> 여유시간!
        if plans[i + 1][1] - plans[i][1] >= plans[i][2]:
            answer.append(plans[i][0])
            freeTime = (plans[i + 1][1] - plans[i][1]) - plans[i][2]
            # stack이 비어있지 않고 여유시간이 0보다 크면
            while stack and freeTime > 0:
                # 가장 최근에 멈춘 과제 꺼내기
                p = stack.pop()
                if freeTime < p[1]:
                    p[1] -= freeTime
                    # 시간 다 씀
                    freeTime = 0
                    stack.append([p[0], p[1]])
                else:
                    freeTime -= p[1]
                    answer.append(p[0])
        else:
            # 다음시간까지 내 과제 수행!
            stack.append([plans[i][0], plans[i][2] - (plans[i + 1][1] - plans[i][1])])

    # 마지막 요소 담기!
    answer.append(plans[-1][0])

    # stack에 남은거는 가장 위에 있는(최신) 과제 부터 빼서 answer에 붙인다.
    return answer + [i[0] for i in stack[::-1]]


"""
새로운 과제 먼저, 멈춰놓은 과제는 최신순
"""
# ["science", "history", "computer", "music"]
solution(
    [
        ["science", "12:40", "50"],
        ["music", "12:20", "40"],
        ["history", "14:00", "30"],
        ["computer", "12:30", "100"],
    ]
)
