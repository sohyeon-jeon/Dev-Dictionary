"""
https://www.acmicpc.net/problem/1593
"""

from itertools import permutations


"""
슬라이딩 윈도우 알고리즘
"""
n, m = map(int, input().split())
w = input()
s = input()

wl = [0] * 52
sl = [0] * 52

# w의 각 알파벳마다 등장하는 부분 +1
for i in range(n):
    if "a" <= w[i] <= "z":
        wl[ord(w[i]) - ord("a")] += 1
    else:
        wl[ord(w[i]) - ord("A") + 26] += 1

start, length, count = 0, 0, 0

for i in range(m):
    if "a" <= s[i] <= "z":
        sl[ord(s[i]) - ord("a")] += 1
    else:
        sl[ord(s[i]) - ord("A") + 26] += 1
    length += 1

    if length == n:
        # wl과 sl의 요소 개수가 같으면 순열로 만들수 있는 글자다!
        if wl == sl:
            count += 1

        if "a" <= s[start] <= "z":
            sl[ord(s[start]) - ord("a")] -= 1
        else:
            sl[ord(s[start]) - ord("A") + 26] -= 1
        start += 1
        length -= 1


print(count)


# 시간초과~
def sol1():
    w_len, s_len = input().split()
    w = input()
    s = input()
    answer = 0

    for p in permutations(w):
        temp = "".join(p)
        if temp in s:
            answer += 1
    print(answer)


"""
즉, 문자열  S안에서 문자열 W의 순열 중 하나가 부분 문자열로 들어있는 모든 경우의 수를 계산하라는 뜻
4 11
cAda
AbrAcadAbRa
"""
