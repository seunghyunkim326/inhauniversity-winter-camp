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
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name
class Charizard(Pokemon, FlyingMixin):
    pass
class Gyarados(Pokemon, SwimmingMixin):
    pass
g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
c1.attack()
# Charizard.attack()      TypeError: Pokemon.attack() missing 1 required positional argument: 'self'
# Charizard.attack(g1)
# print(g1.name)
# g1.name = "잉어킹"
# print(g1.name)              #왜 위에서 g1 객체 생성 시 "갸라도스"라고 name변수를 지정해 준 것이 아닌가? => g1.name은 변수 자리이고 g1 객체를 생성할 때와 같이 self자리에는 g1 객체가 상응한다고 생각하면 된다.
print(g1.get_name())
g1.set_name("잉어킹")
print(g1.get_name())
# print(g1.set_name())        #TypeError: Pokemon.set_name() missing 1 required positional argument: 'new_name'   두줄 위에서 지정해 주었지만 왜 new_name 변수를 지정하라고 하는 것인가?
g1.set_name("붕어빵")
print(g1.get_name())
# g1 = Gyarados("갸라도스")
# TypeError: Pokemon.__init__() takes 1 positional argument but 2 were given     self라는 객체 뒤에 매개 변수(name)을 통해 변수를 받아들여야한다.