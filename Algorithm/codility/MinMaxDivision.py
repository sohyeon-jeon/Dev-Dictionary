def solution(K, M, A):
    def feasible(large_sum):
        block_sum = 0
        block_count = 0

        for num in A:
            # 블록의 합계가 mid보다 크면 새로운 블록을 시작한다
            if block_sum + num > large_sum:
                block_sum = num
                block_count += 1
            else:
                block_sum += num

            # If the number of blocks exceeds K, it's not feasible
            if block_count >= K:
                return False

        return True

    """
    이분탐색
    lower_bound를 배열의 최대값으로
    upper_bound는 배열의 합계로 설정
    """
    lower_bound = max(A)
    upper_bound = sum(A)
    result = upper_bound

    # Binary search
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2

        # 현재 중간값으로 블록을 생성할 수 있는 지 판단
        if feasible(mid):
            result = mid
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1

    return result


# [2, 1], [5, 1], [2, 2, 2]의
# 목표는 큰 합계를 최소화하는 것입니다. 위의 예에서 6이 최소 큰 합계입니다.
solution(3, 5, [2, 1, 5, 1, 2, 2, 2])
