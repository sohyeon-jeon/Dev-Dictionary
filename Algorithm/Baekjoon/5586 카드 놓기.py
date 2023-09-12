"""
https://www.acmicpc.net/problem/5568
"""
from itertools import permutations

n = int(input())
k = int(input())
cards = []
card_set = set()

for _ in range(n):
    cards.append(input())

for num in permutations(cards, k):
    card_set.add("".join(num))
print(len(card_set))


"""
n장의 카드에 적힌 숫자가 주어졌을 때, 그 중에서 k개를 선택해서 만들 수 있는 정수의 개수를 구하는 프로그램을 작성하시오.

4
2
1
2
12
1

7

"""
