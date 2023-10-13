"""
https://school.programmers.co.kr/learn/courses/30/lessons/172927
"""
from collections import defaultdict


# 정확성 42.9 -> 테케 몇개 실패
def solution1(picks, minerals):
    answer = 0
    # [dia, iron, stone]
    consume = defaultdict(dict)
    consume["diamond"] = {"diamond": 1, "iron": 1, "stone": 1}
    consume["iron"] = {"diamond": 5, "iron": 1, "stone": 1}
    consume["stone"] = {"diamond": 25, "iron": 5, "stone": 1}

    tools = ["diamond"] * picks[0] + ["iron"] * picks[1] + ["stone"] * picks[2]

    for i in range(len(minerals)):
        if i >= len(tools) * 5:
            break
        tool = tools[i // 5]
        answer += consume[tool][minerals[i]]

    return answer


def solution(picks, minerals):
    answer = 0

    # 캐야할 광석이 곡괭이 * 5보다 크면 광석을 캘 수 없다.
    # 정렬 전에 미리 잘라주기
    if len(minerals) > sum(picks) * 5:
        minerals = minerals[: sum(picks) * 5]

    new_mineral = [[0, 0, 0] for _ in range(len(minerals) // 5 + 1)]
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            new_mineral[i // 5][0] += 1
        elif minerals[i] == "iron":
            new_mineral[i // 5][1] += 1
        elif minerals[i] == "stone":
            new_mineral[i // 5][2] += 1

    # 광물은 주어진 순서대로만 캘 수 있습니다.
    """
    광물은 순서대로 캐야 한다!
    곡괭이는 바꿀 수 있다.

    최소 피로도로 하려면 다이아몬드,철,돌 광물이 많은 순으로 정렬해서 다이아몬드,철,돌 곡괭이 무기순으로 처리하는게 좋다!
    """
    new_mineral = sorted(new_mineral, key=lambda x: (-x[0], -x[1], -x[2]))

    for i in range(len(new_mineral)):
        # 곡괭이 다이아몬드,철,돌 순으로 처리
        if picks[0] > 0:
            answer += new_mineral[i][0] + new_mineral[i][1] + new_mineral[i][2]
            picks[0] -= 1
        elif picks[1] > 0:
            answer += (5 * new_mineral[i][0]) + new_mineral[i][1] + new_mineral[i][2]
            picks[1] -= 1
        elif picks[2] > 0:
            answer += (
                (25 * new_mineral[i][0]) + (5 * new_mineral[i][1]) + new_mineral[i][2]
            )
            picks[2] -= 1

        # 더 이상 사용할 무기가 없다면 더 이상 진행하지 못함
        if sum(picks) == 0:
            break

    return answer


# 50
solution(
    [0, 1, 1],
    [
        "diamond",
        "diamond",
        "diamond",
        "diamond",
        "diamond",
        "iron",
        "iron",
        "iron",
        "iron",
        "iron",
        "diamond",
    ],
)

"""
마인은 곡괭이로 광산에서 광석을 캐려고 합니다. 마인은 다이아몬드 곡괭이, 철 곡괭이, 돌 곡괭이를 각각 0개에서 5개까지 가지고 있으며, 곡괭이로 광물을 캘 때는 피로도가 소모됩니다. 각 곡괭이로 광물을 캘 때의 피로도는 아래 표와 같습니다.

image

예를 들어, 철 곡괭이는 다이아몬드를 캘 때 피로도 5가 소모되며, 철과 돌을 캘때는 피로도가 1씩 소모됩니다. 각 곡괭이는 종류에 상관없이 광물 5개를 캔 후에는 더 이상 사용할 수 없습니다.

마인은 다음과 같은 규칙을 지키면서 최소한의 피로도로 광물을 캐려고 합니다.

사용할 수 있는 곡괭이중 아무거나 하나를 선택해 광물을 캡니다.
한 번 사용하기 시작한 곡괭이는 사용할 수 없을 때까지 사용합니다.
광물은 주어진 순서대로만 캘 수 있습니다.
광산에 있는 모든 광물을 캐거나, 더 사용할 곡괭이가 없을 때까지 광물을 캡니다.
즉, 곡괭이를 하나 선택해서 광물 5개를 연속으로 캐고, 다음 곡괭이를 선택해서 광물 5개를 연속으로 캐는 과정을 반복하며, 더 사용할 곡괭이가 없거나 광산에 있는 모든 광물을 캘 때까지 과정을 반복하면 됩니다.

마인이 갖고 있는 곡괭이의 개수를 나타내는 정수 배열 picks와 광물들의 순서를 나타내는 문자열 배열 minerals가 매개변수로 주어질 때, 마인이 작업을 끝내기까지 필요한 최소한의 피로도를 return 하는 solution 함수를 완성해주세요.

제한사항
picks는 [dia, iron, stone]과 같은 구조로 이루어져 있습니다.
0 ≤ dia, iron, stone ≤ 5
dia는 다이아몬드 곡괭이의 수를 의미합니다.
iron은 철 곡괭이의 수를 의미합니다.
stone은 돌 곡괭이의 수를 의미합니다.
곡괭이는 최소 1개 이상 가지고 있습니다.
5 ≤ minerals의 길이 ≤ 50
minerals는 다음 3개의 문자열로 이루어져 있으며 각각의 의미는 다음과 같습니다.
diamond : 다이아몬드
iron : 철
stone : 돌
입출력 예
picks	minerals	result
[1, 3, 2]	["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]	12
[0, 1, 1]	["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]	50
"""
