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
pickachu = Pokemon("피카츄")
squirtle = Pokemon("꼬부기")
print(pickachu)
print(squirtle)