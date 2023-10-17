def solution(sequence, k):
    left = right = 0
    answer = [0, len(sequence)]
    sum = sequence[0]

    while True:
        if sum < k:
            right += 1
            if right == len(sequence):
                break
            sum += sequence[right]
        else:
            if sum == k:
                if right - left < answer[1] - answer[0]:
                    answer = [left, right]

            sum -= sequence[left]
            left += 1
    return answer


# [6,6]
solution([1, 1, 1, 2, 3, 4, 5], 5)

"""
left,right 각각 0부터 시작
sum은 첫번째 숫자부터 시작
sum<k면 / right+=1, sum+=arr[sum]
sum>k면 / sum-=arr[sum], left+=1,
sum==k면 / 정답 리프레쉬, sum-=arr[sum], left+=1
"""
