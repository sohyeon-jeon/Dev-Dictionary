"""
https://school.programmers.co.kr/learn/courses/30/lessons/12981
"""


def solution(n, words):
    for i in range(1, len(words)):
        # 마지막 단어와 다르거나 기존에 말했던 단어면 탈락
        if (words[i - 1][-1] != words[i][0]) or (words[i] in words[:i]):
            return [i % n + 1, i // n + 1]
    return [0, 0]


solution(
    3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
)
