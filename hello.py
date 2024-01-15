# 섭씨온도 화씨온도 변환 프로그램 3번 눌러서 탈출
# (100°F − 32) × 5/9 = 37.778°C
# (0°C × 9/5) + 32 = 32°F
while True:
    menu = int(input("1) Fahrenheit -> Celsius 2) Celsius -> Fahrenheit 3) quit program : "))
    if menu == 1:
        fahrenheit = int(input("Input Fahrenheit : "))
        print((fahrenheit - 32)*5/9)
    elif menu == 2:
        celsius = int(input("Input Celsius : "))
        print((celsius*9/5)+32)
    elif menu == 3:
        break