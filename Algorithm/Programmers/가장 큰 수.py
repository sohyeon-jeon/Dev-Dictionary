def solution(numbers):
    numbers = list(map(str, numbers))
    # x*3 -> 인수값이 1000이하이므로 3배 늘려서 비교
    # 아스키 문자로 비교, 첫 인덱스를 가지고 비교 , reverse=True 옵션 켜주어야함
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(numbers)))


solution([6, 10, 2])
