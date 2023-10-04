"""
https://school.programmers.co.kr/learn/courses/30/lessons/42884
"""


def solution(routes):
    camera = 0
    # 끝점을 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    end_point = -30001
    for route in routes:
        # 끝점이 현재시작점보다 작다면 만나지 못했다 -> 카메라 추가 설치
        if end_point < route[0]:
            camera += 1
            end_point = route[1]
    return camera


solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]])
