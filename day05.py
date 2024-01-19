# class Pokemon:
#     def __init__(self, name):
#         self.name = name
#     def attack(self, target):
#         print(f"{self.name}이(가) {target.name}을(를) 공격!")
# # class Pikachu:
# class Pikachu(Pokemon):     # is-a
#     def attack(self, target):
#         print(f"{self.name}이(가) {target.name}을(를) 일렉트릭 공격")
#     def electric_info(self):
#         print(("전기 계열의 공격을 합니다"))
# class Agumon:
#     pass
# p1 = Pikachu("피카츄")
# p2 = Agumon("아구몬")
#
# print(p1.name)
# print(issubclass(Pikachu, Pokemon))
# print(issubclass(Agumon, Pokemon))

class Animal:
    def says(self):
        return 'I speak!'
class Horse(Animal):
    # def says(self):
    #     return 'Neigh'
    pass
class Donkey(Animal):
    def says(self):
        return  'Hee-haw!'
class Mule(Horse):
    pass
class Hinny(Horse, Donkey):
    pass
m1 = Mule()
h1 = Hinny()
print(h1.says())
print(m1.says())
print(Hinny.__mro__)
print(Mule.__mro__)