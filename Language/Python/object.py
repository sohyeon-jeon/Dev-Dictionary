class Test1:
    s = "abc"
    lst = []

    def test():
        # 함수 내부에서 전역 변수를 수정하거나 참조할 떄 사용
        global s
        s += "123"
        return s

    # test()
    # print(s)


def outer():
    x = 10

    def inner():
        # 중첩된 함수에서 가장 가까운 외부함수의 변수를 참조하거나 수정
        nonlocal x
        x += 5
        print(x)

    inner()


outer()
