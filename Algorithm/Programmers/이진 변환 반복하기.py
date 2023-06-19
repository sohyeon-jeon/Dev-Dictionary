'''
https://school.programmers.co.kr/learn/courses/30/lessons/70129
'''

class Test1:
    def solution(s):
        cnt=0
        del_zero=0
        while True:
            del_zero+=s.count('0')
            s=s.replace('0','')
            s=bin(len(s))[2:]
            cnt+=1
            if s=="1":
                return [cnt,del_zero]

def radix_transformation(number,base):
    result=''
    while number>0:
        number,mod=divmod(number,base)
        result+=str(mod)
    return result[::-1]


def solution(s):
    cnt=0
    del_zero=0
    while True:
        del_zero+=s.count('0')
        s=s.replace('0','')
        s=radix_transformation(len(s),2)
        cnt+=1
        if s=="1":
            return [cnt,del_zero]


solution("110010101001")