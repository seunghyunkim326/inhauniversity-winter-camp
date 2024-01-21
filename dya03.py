class FlyingMixin:
    def fly(self):
        return f"{self.name}이(가) 하늘을 훨훨 날아갑니다~"
class SwimmingMixin:
    def swim(self):
        return f"{self.name}이(가) 수영을 합니다."
class Pokemon:
    def __init__(self, name):
        self.name = self
    def attack(self):
        print("공격!!")
class Charizard(Pokemon, FlyingMixin):
    pass
class Gyarados(Pokemon, SwimmingMixin):
    pass
g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
c1.attack()
# Charizard.attack()      TypeError: Pokemon.attack() missing 1 required positional argument: 'self'
# Charizard.attack(g1)
print(g1.name)
g1.name = "잉어킹"
print(g1.name)              #왜 위에서 g1 객체 생성 시 "갸라도스"라고 name변수를 지정해 준 것이 아닌가?
# g1 = Gyarados("갸라도스")
# TypeError: Pokemon.__init__() takes 1 positional argument but 2 were given     self라는 객체 뒤에 매개 변수(name)을 통해 변수를 받아들여야한다.