"""
https://www.acmicpc.net/problem/10814
"""
n = int(input())
members = []
for i in range(n):
    age, name = input().split()
    members.append([i, int(age), name])

members = sorted(members, key=lambda x: (x[1], x[0]))

for i, age, name in members:
    print(age, name)

"""
온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.
3
21 Junkyu
21 Dohyun
20 Sunyoung

20 Sunyoung
21 Junkyu
21 Dohyun
"""
