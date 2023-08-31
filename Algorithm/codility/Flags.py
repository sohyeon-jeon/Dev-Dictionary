# 66점  , timeout
def solution1(A):
    N = len(A)
    peak = []
    max_peak = 0

    # peak 구하기
    for i in range(1, N - 1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            peak.append(i)

    if len(peak) < 2:
        return len(peak)

    for k in range(2, len(peak) + 1):
        current_flag = 1
        pre_peak = peak[0]

        for j in range(len(peak)):
            if peak[j] - pre_peak >= k:
                current_flag += 1
                pre_peak = peak[j]
            if current_flag > k:
                current_flag = k
                break
        max_peak = max(max_peak, current_flag)
    return max_peak


import math


def solution(A):
    N = len(A)

    # 배열이 3보다 작은 경우에는 peak을 구할 수 없다.
    if len(A) < 3:
        return 0

    peak = []

    for i in range(1, N - 1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            peak.append(i)

    if len(peak) < 3:
        return len(peak)

    # 젤 처음과 마지막 peak사이에 꽂을 수 있는 깃발 수
    max_flag = int(math.sqrt(peak[-1] + peak[0])) + 1
    print(max_flag)

    for f in range(max_flag, 2, -1):
        count = 1
        p = peak[0]
        for i, pe in enumerate(peak):
            if f <= pe - p:
                count += 1
                p = pe

        if count >= f:
            break
    return f


# peak : 1 3 5 10
# k개의 깃발을 가져간다면 모든 두 깃발간의 거리는 k보다 크거나 같아야한다.
solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2])

"""
flag 수에 따라서 최소한으로 요구하는 배열크기는 아래와 같습니다.
1
X P X => 3
2
X P X P X => 5
3
X P XX P XX P X => 9
4
X P XXX P XXX P XXX P X => 15
5
X P XXXX P XXXX P XXXX P XXXX P X => 23
6
X P XXXXX P XXXXX P XXXXX P XXXXX P XXXXX P X => 33


최소 요구 배열크기(minimally required SizeOfArray)를 MRS(N)라고 할 때,
MRS(N) = MRS(N - 1) + (N - 1)*2 (when N > 1), MRS(1) = 3 라는 식이 성립합니다.

MRS(N) = (N - 1)*2 + (N - 2)*2 + (N - 3)*2 + ... + 3*2 + 2*2 + 1*2 + 3 = (N - 1)*(N - 1 + 1) + 3 = (N - 1)*N + 3
∴ MRS(N) = N^2 - N + 3 ≤ N^2 (when N ≥ 3)

대략적으로 MRS(N) = N^2라고 해도 무방합니다.
즉, 3개의 깃발이 필요할 때는, 최소한 배열의 사이즈는 9개 이상이여야 합니다.

반대로 사이즈에 따라서 최대로 가능한 깃발의 수는 
MRS(N)의 역함수를 구하면 됩니다.

∴ MRS^{-1}(N) = N^{1/2} (N의 제곱근)
<example> MRS^{-1}(9) = 3, MRS^{-1}(16) = 4

따라서, 첫번째 peak와 마지막 peak의 차를 구하면 실질적인 배열의 수를 알 수 있고, 
이 배열의 수에 제곱근을 한다면, 최대로 가능한 flat수를 알 수 있습니다.

대략적으로, MRS^{-1}(N) = N^{1/2}에서 +1을 하여 3.8xxx와 같은 값이 나올 때, 3 + 1로 최대 flag수를 지정하고 for문을 돌립니다.
<example> MPN(8) = 3, MPN(9) = 4, MPN(15) = 4, MPN(16) = 5
"""
