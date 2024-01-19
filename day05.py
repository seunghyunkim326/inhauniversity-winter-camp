def test(f):
    '''
    데코레이터 함수, 함수 시작 시 start 출력, 함수 끝날 시 end 출력
    :param f: function
    :return: closure function
    '''
    def test_in(*args, **kwargs):       # *args : 무한한 변수 갯수     **kwargs : dictionary 형태로 받고 싶을 때
        print('start')
        r = f(*args, **kwargs)
        print('end')
        return r
    return test_in

#
# def greeting():
#     print("Hello")
# t = test(greeting)
# t()

@test
def greeting():
    print("Hello")
greeting()