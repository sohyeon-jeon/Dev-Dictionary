### immutable  
 - 변경되지 않는 객체
 - 만약 99를 100으로 바꾼다면, 값이 변경되는 게 아니라 100인 객체를 생성해서 100을 참조하는 것이다.
 - int 타입은 값이 변경되면 같은 객체를 참조하지만, str의 경우에는 항상 같은 곳을 참조하지는 않는다.
 - int, float, str, tuple, bool

 ``` python
 s1 = "BlockMask"
print(hex(id(s1)))
s2 = "BlockMask"
print(hex(id(s2)))
s3 = "BlockMask"
print(hex(id(s3)))

s1 = "BlockZZZMask"
print(hex(id(s1)))

s2 = "BlockZZZMask"
print(hex(id(s2)))

s3 = s3.replace("D", "ZZZ")
print(hex(id(s3)))

'''
0x7fa12d183d30
0x7fa12d183d30
0x7fa12d183d30

0x7fa12d183df0
0x7fa12d183df0
0x7fa12d183d30
'''

 ```

 ### mutable
 - 변경되는 객체
 - list, set, dictionary

