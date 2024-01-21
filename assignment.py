# 10.15 3)
# Thing3 클래스 생성 이 클래스 letters 속성에 값 'xyz' 할당 후 letters 출력, letters 출력을 위해 객체 생성해야 하나? => 필요함
class Thing3:
    def __init__(self, letter):
        self.letters = letter
A = Thing3('xyz')
print(A)
print(A.letters)