"""
# permutations(순열) : n개의 원소에서 중복을 허용하지 않고 r개를 뽑아서 나열
from itertools import permutations

for i in permutations([1,2,3,4],2):
    print(i,end=' ')
# (1, 2) (1, 3) (1, 4) (2, 1) (2, 3) (2, 4) (3, 1) (3, 2) (3, 4) (4, 1) (4, 2) (4, 3)
"""
def permutations(array,r):
    for i in range(len(array)):
        if r==1:
            yield [array[i]]
        else:
            # 선택한 원소를 제외한 나머지 원소를 이용하여 r-1의 순열을 만든다.
            for next in permutations(array[:i]+array[i+1:],r-1):
                yield [array[i]]+next

"""
중복순열
from itertools import product

for i in product([1, 2, 3], 'ab'):
    print(i, end=" ")
    (1, 'a') (1, 'b') (2, 'a') (2, 'b') (3, 'a') (3, 'b')
"""
def dupli_permu(array,r):
    for i in range(len(array)):
        if r==1:
            yield [array[i]]
        else:
            # 선택한 원소를 제외한 나머지 원소를 이용하여 r-1의 순열을 만든다.
            for next in dupli_permu(array[:i]+array[i:],r-1):
                yield [array[i]]+next

print(list(dupli_permu([1,2,3,4],2)))
 

    
"""
# combinations(조합) : n개의 원소에서 중복을 허용하지 않고, r개를 뽑음
from itertools import combinations

for i in combinations([1,2,3,4],2):
    print(i,end=' ')
# (1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4)
"""

def combinations(array,r):
    for i in range(len(array)):
        if r==1:
            yield [array[i]]
        else:
            for next in combinations(array[i+1:],r-1):
                yield [array[i]]+next

"""
중복조합
from itertools import combinations_with_replacement

for i in combinations_with_replacement([1, 2, 3, 4], 2):
    print(i, end=" ")
"""
def dupli_combi(array,r):
    for i in range(len(array)):
        if r==1:
            yield [array[i]]
        else:
            for next in dupli_combi(array[i:],r-1):
                yield [array[i]]+next

# print(list(dupli_combi([1,2,3,4],2)))
# [[1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [2, 4], [3, 3], [3, 4], [4, 4]]


