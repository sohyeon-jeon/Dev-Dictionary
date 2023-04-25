from collections import deque

def solution(queue1, queue2):
    answer=0

    q1=deque(queue1)
    q2=deque(queue2)
    sum1=sum(q1)
    sum2=sum(q2)
    if (sum1+sum2)%2!=0:
        return -1
    
    # 최악의 상황 queue1과 queue2의 원소를 모두 바꾸는 경우 4*len(queue1) // queue1과 queue2의 길이는 같다
    
    for _ in range(4*len(queue1)):
        if sum1==sum2:
            return answer
        elif sum1<sum2:
            sum1+=q2[0]
            sum2-=q2[0]
            q1.append(q2.popleft())
        
        elif sum1>sum2:
            sum2+=q1[0]
            sum1-=q1[0]            
            q2.append(q1.popleft())
        else:
            return answer
        answer+=1
    return -1
        
solution([1,4],[4,8])

'''
- list의 pop(0)를 사용하면 시간 복잡도가 상승해서 시간 초과의 위험이 있기에 deque의 popleft()를 사용했다.
- 최적의 해를 찾기 위해 리스트의 값이 큰 쪽에서 작은 쪽으로 옮긴다.
- queue1과 queue2의 원소를 모두 바꾸는 경우 queue1 길이의 2배만큼 횟수가 필요하고 다시 모든 원소를 바꿔 원래의 모습으로 만들면 queue1 길이의 2배만큼 필요해 총 len(queue1) * 4 만큼 횟수가 필요하다.
- 그래서 4*len(queue1) 제한 조건을 두었다.
- sum 함수도 계속 쓰면 시간 초과가 나므로, 변수에서 뺴주는 방식으로 진행
- 시간초과 챙기기!! 제한조건 break


'''