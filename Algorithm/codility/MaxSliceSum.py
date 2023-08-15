def solution(A):
    # 현재 요소를 포함하는 연속적인 부분 배열의 최대 합 max_ending_here
    # 지금까지 발견한 최대 합 max_so_far
    max_ending_here = max_so_far = A[0]
    
    for num in A[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

        
    return max_so_far