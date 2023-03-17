'''
https://school.programmers.co.kr/learn/courses/30/lessons/155651
'''
def time2val(time):
    return int(time[:2]) * 60 + int(time[3:5])
def solution(book_time):
    dic = {}
    for book in book_time:
        st = time2val(book[0])
        en = time2val(book[1])
        for t in range(st,en+10):
            if dic.get(t) == None:
                dic[t] = 1
            else:
                dic[t] += 1
    
    return max(dic.values())

solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])
'''
시간을 분으로 바꿔서 대실 시간동안의 분마다 +=1
최종적으로 max(dic.values()) 출력하면 코니에게 필요한 최소 객실의 수를 구할 수 있음!
'''