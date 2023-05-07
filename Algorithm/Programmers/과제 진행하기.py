def solution(plans):
    answer = []
    stack=[]
    for i in range(len(plans)):
        t,m=map(int,plans[i][1].split(':'))
        plans[i][1]=t*60+m
        plans[i][2]=int(plans[i][2])
    plans=sorted(plans,key=lambda x:x[1])

    for i in range(len(plans)-1):
        # 다음 과제까지 남은 시간이 내 과제 소요시간보다 길면
        if plans[i+1][1]-plans[i][1]>=plans[i][2]:
            freeTime=plans[i+1][1]-plans[i][1]-plans[i][2]
            answer.append(plans[i][0])
            while stack and freeTime>0:
                # 가장 최근에 멈춘 study부터 꺼내기
                reStudy=stack.pop()
                # freeTime이 reStudy 소요시간보다 크면 해당 스터디 처리
                if freeTime>=reStudy[1]:
                    freeTime-=reStudy[1]
                    answer.append(reStudy[0])
                # 아니면 여유 시간동안만 해당 study 진행
                else:
                 
                    reStudy[1]-=freeTime
                    freeTime=0
                    stack.append(reStudy)

        else:
            stack.append([plans[i][0],plans[i][2]-(plans[i+1][1]-plans[i][1])])

    # 마지막 요소 담기
    answer.append(plans[-1][0])
    
    # stack에 남은 것 최근꺼부터 담기! 
    while stack:
        answer.append(stack.pop()[0])

    return answer

solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]])