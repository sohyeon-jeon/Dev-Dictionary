'''
https://school.programmers.co.kr/learn/courses/30/lessons/12980
'''

class Test1:
    def solution(n):
        ans = 0
        
        while True:
            if n==0:
                break
            
            if n%2==0:
                n//=2
            else:
                n-=1
                ans+=1

        print(ans)
        return ans


class Test2:
    def solution(n):
        return bin(n).count('1')
    