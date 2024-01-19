class Pokemon():
    def __init__(self):
        pass
pickachu = Pokemon()
squirtle = Pokemon()
pickachu.name = "피카츄"
pickachu.nemesis = squirtle
print(pickachu.name)
# print(pickachu.nemesis.name)
pickachu.nemesis.name = "꼬부기"
print(pickachu.nemesis.name)
print(squirtle.name)