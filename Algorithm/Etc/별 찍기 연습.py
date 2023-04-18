'''
* 파이썬 포매팅
< 왼쪽 정렬
> 오른쪽 정렬
^ 가운데 정렬
'''

'''
1.
*    
**   
***  
**** 
*****
'''
def one():
    for i in range(5):
        for _ in range(i+1):
            print('*',end='')
        print()

    for i in range(5):
        print('{:<5}'.format('*'*(i+1)))

'''
2.
*****
****
***
**
*
'''
def two():
    for i in range(5,0,-1):
        for _ in range(i):
            print('*',end='')
        print()

    for i in range(5,0,-1):
        print('{:<5}'.format('*'*i))

'''
3.
*****
 ****
  ***
   **
    *
'''
def three():
    for i in range(5):
        for _ in range(i):
            print(' ',end='')
        for _ in range(5-i):
            print('*',end='')
        print()

    for i in range(5,0,-1):
        print('{:>5}'.format('*'*i))

'''
4.
    *
   **
  ***
 ****
*****
'''
def four():
    for i in range(1,6):
        for _ in range(5-i):
            print(' ',end='')
        for _ in range(i):
            print('*',end='')
        print()

    for i in range(5):
        print('{:>5}'.format('*'*(i+1)))

'''
5.
    *
   ***
  *****
 *******
*********
'''
def five():
    for i in range(5):
        print(' '*(5-i-1)+'*'*(2*i+1))

    for i in range(1,11,2):
        print('{:^10}'.format('*'*i))
'''
6.
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
'''
def six():
    for i in range(1,6):
        for j in range(5-i):
            print(' ',end="")
        for j in range(1,i*2,1):
            print('*',end="")
        print('')

    for i in range(5):
        for j in range(i):
            print(' ',end="")
        for j in range(10,1+i*2,-1):
            print('*',end="")
        print('')
    
    for i in range(1, 11, 2):
        print('{:^10}'.format('*' * i))
    for i in range(9, 0, -2):
        print('{:^10}'.format('*' * i))
'''
7.
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
'''
def seven():
    for i in range(5):
        for j in range(i):
            print(' ',end='')
        for j in range(10,(2*i)+1,-1):
            print('*',end='')
        print()

    for i in range(2,6):
        for j in range(5-i):
            print(' ',end='')
        for j in range(1,2*i,1):
            print('*',end='')
        print()

    for i in range(9, 0, -2):
        print('{:^10}'.format('*' * i))
    
    for i in range(3, 11, 2):
        print('{:^10}'.format('*' * i))



