'''
https://school.programmers.co.kr/learn/courses/30/lessons/17686
'''
class Test1:
    def solution(files):
        tmp = []
        head, number, tail = '', '', ''
        
        for file in files:       
            for i in range(len(file)):
                if file[i].isdigit():     # 숫자가 나오면 그 이전은 무조건 HEAD, 이후는 NUMBER, TAIL로 다시 구분
                    head = file[:i]
                    number = file[i:]
                    
                    for j in range(len(number)):    # NUMBER와 TAIL 구분 (숫자 안나오면 TAIL)
                        if not number[j].isdigit():
                            tail = number[j:]
                            number = number[:j]
                            break
                            
                    tmp.append([head, number, tail])
                    head, number, tail = '', '', ''
                    break
        answer=sorted(tmp,key=lambda x:( x[0].lower(),int(x[1]) ))
        return [''.join(i) for i in answer]


'''
정규표현식 사용
'''
import re

def solution(files):

    def key_function(fn):
        head,number,tail = re.match(r'([a-z-. ]+)(\d{,5})(.*)',fn).groups()
        return [head,int(number)]

    print(sorted(files, key = lambda x: key_function(x.lower())))
    return sorted(files, key = lambda x: key_function(x.lower()))



        


# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
solution(["foo9.txt","foo010bar020.zip","F-15"])