# class Pokemon():
#     def __init__(self):
#         pass
# pickachu = Pokemon()
# squirtle = Pokemon()
# pickachu.name = "피카츄"
# pickachu.nemesis = squirtle
# print(pickachu.name)
# # print(pickachu.nemesis.name)
# pickachu.nemesis.name = "꼬부기"
# print(pickachu.nemesis.name)
# print(squirtle.name)

class Pokemon:
    def __init__(self, name):
        self.name = name
        print(f"{name} 포켓몬스터 생성")
    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")
charizard = Pokemon("리자몽")
pickachu = Pokemon("피카츄")
squirtle = Pokemon("꼬부기")

charizard.attack(squirtle)
print(pickachu.name)
print(squirtle.name)