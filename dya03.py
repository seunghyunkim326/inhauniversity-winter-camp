import random
drinks_food = {'위스키': "초콜릿", "와인": "치즈", "소주": "삼겹살", "고량주": "양꼬치"}
# print(drinks_food)
# print(drinks_food.pop("고량주"))
# print(drinks_food)
# del drinks_food["위스키"]
# drinks_food["사케"] = "광어회"
japan_drinks_foods = {"사케" : '광어회', '위스키': '낙곱새'}
drinks_food.update(japan_drinks_foods)
# drink = input(drinks_food.keys())
drinks_food_keys = list(drinks_food)
# print(drinks_food_keys)
# # print(drinks_food_keys.pop(0))
# print(drinks_food_keys.remove("위스키"))
# print(drinks_food_keys)
# print(drinks_food_keys)
# print(random.choice(drinks_food_keys))
while True:
    menu = input(f'다음 술중에 고르시오.\n1) {drinks_food_keys[0]} 2) {drinks_food_keys[1]} 3) {drinks_food_keys[2]} 4)아무거나 5) 종료: ')
    if menu == '1':
        print(f"{drinks_food_keys[0]}에 어울리는 안주는 {drinks_food[drinks_food_keys[0]]} 입니다.")
    elif menu == '2':
        print(f"{drinks_food_keys[1]}에 어울리는 안주는 {drinks_food[drinks_food_keys[1]]} 입니다.")
    elif menu == '3':
        print(f"{drinks_food_keys[2]}에 어울리는 안주는 {drinks_food[drinks_food_keys[2]]} 입니다.")
    elif menu == '4':
        random_drink = random.choice(drinks_food_keys)
        print(f'{random_drink}에 어울리는 안주는 {drinks_food[random_drink]} 입니다.')
    elif menu == '5':
        print(f"다음에 또 오세요")
        break