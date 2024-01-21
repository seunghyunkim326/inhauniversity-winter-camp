# 10.15 2)
# Thing2 클래스 생성 이 클래스 letters 속성에 값 'abc' 할당 후 letters 출력
class Thing2:
    def __init__(self, letter):
        self.letters = letter
A = Thing2('abc')
print(A.letters)