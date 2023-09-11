def solution(s):
    answer = []

    # 글자를 끊을 단위 i
    for i in range(1, len(s) + 1):
        new_str = ""
        cnt = 1
        word = s[:i]

        for j in range(i, len(s) + i, i):
            if word == s[j : i + j]:
                cnt += 1
            else:
                if cnt == 1:
                    new_str += word
                else:
                    new_str += str(cnt) + word

                word = s[j : i + j]
                cnt = 1
        answer.append(len(new_str))

    return min(answer)


# 2a2ba3c
solution("aabbaccc")
"""
ab
cd
cd
ab
ab
cd
cd
"""
