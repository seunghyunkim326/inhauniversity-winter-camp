class Pokemon:
    def __init__(self, name):
        self.name = name
        print(f"{name} 포켓몬스터 생성")
    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")
class Pikachu(Pokemon):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) {self.type} 공격!")
    def electric_info(self):
        print("전기 계열의 공격을 합니다")