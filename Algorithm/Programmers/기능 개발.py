import math

class Test1:
    def solution(progresses, speeds):
        answer = []
        days=[]
        # 남은 일수 days 리스트에 넣기
        for i in range(len(progresses)):
            days.append(math.ceil((100-progresses[i])/speeds[i]))
        
        # idx(비교)
        idx=0
        for i in range(len(days)):
            if days[i]>days[idx]:
                answer.append(i-idx)
                idx=i
        answer.append(len(days)-idx)
        return answer
    
def solution(progresses, speeds):
    answer = []
    count=0
    time=0
    while progresses:
        if progresses[0]+time*speeds[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            count+=1
        else:
            if count>0:
                answer.append(count)
                count=0
            time+=1
    answer.append(count)
    return answer

solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])