'''
https://school.programmers.co.kr/learn/courses/30/lessons/49993
'''
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer


# 2
solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])

