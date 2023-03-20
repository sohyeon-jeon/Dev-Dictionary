'''
N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.
입력
첫 번째 줄에 학생의 수 N이 입력된다. (1<= N <= 100,000)

두 번째 줄부터 N + 1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다. 문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.

출력
모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.
<입력 예시>
2
홍길동 95
이순신 77

<출력 예시>
이순신 홍길동
'''
n=int(input())
students=[]
for i in range(n):
    data=input().split()
    students.append((data[0],int(data[1])))
result=sorted(students,key=lambda x:x[1])
for r in result:
    print(r[0],end=' ')
'''
학생의 정보가 최대 100,000개까지 입력될 수 있다. 
최악의 경우 O(nlogn)을 보장하는 알고리즘을 이용하거나 O(n)을 보장하는 계수정렬을 이용하면 된다.
'''
