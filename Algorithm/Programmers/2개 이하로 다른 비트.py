'''
https://school.programmers.co.kr/learn/courses/30/lessons/77885
'''
'''
Tip
1. 짝수 -> 이진수 변환 끝자리가 항상 0 -> 끝 자리 1로 바꿔주면 됨
2. 홀수 -> 뒤에부터 맨 처음 0을 만나면, 0을 1로 바꿔주고 그다음 비트를 0으로 바꿔주면 된다.
ex -> 9(1001) 은 1001 -> 1011 -> 1010 으로 10
* rindex() -> 지정 문자열이 마지막 나타나는 위치 반환.
'''

def solution(numbers):
    answer=[]
    for num in numbers:
        if num%2==0:
            answer.append(num+1)
        else:
            number_bin = '0' + bin(num)[2:]
            number_bin=number_bin[:number_bin.rindex('0')]+'10'+number_bin[number_bin.rindex('0')+2:]
            answer.append(int(number_bin, 2))
    return answer
            


# 테케 10,11 시간초과
class Test1:
    def solution(numbers):
        answer = []
        for num in numbers:
            i=num
            while True:
                i+=1
                b_num,b_i=bin(num)[2:],bin(i)[2:]
                max_length=max(len(b_num),len(b_i))

                b_num=b_num.zfill(max_length)
                b_i=b_i.zfill(max_length)
                diff_cnt=sum([a!=b for a,b in zip(b_num,b_i)])

                if diff_cnt<=2:
                    answer.append(i)
                    break
        return answer

solution([2,7])

