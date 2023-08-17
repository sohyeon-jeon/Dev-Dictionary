def solution(A):
    target=len(A)//2
    counter_dict=defaultdict(int)
   
    for i,v in enumerate(A):
        counter_dict[v]+=1
        if counter_dict[v]>target:
            return i
    else:
        return -1

# 라이브러리 안쓰고 
def solution(A):
    counter_dict={}
    for i,v in enumerate(A):
        if not v in counter_dict:
            counter_dict[v]=1
        else:
            counter_dict[v]+=1
        
        if counter_dict[v]>(len(A)//2):
            return i
    else:
        return -1