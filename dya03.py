# (100°F − 32) × 5/9 = 37.778°C
# (0°C × 9/5) + 32 = 32°F
while True:
    menu = int(input("1) Fahrenheit -> Celsius 2) Celsius -> Fahrenheit 3) decide a prime number 4) find all prime numbers 5) quit : "))
    if menu == 1:
        fahrenheit = int(input("Input Fahrenheit : "))
        print((fahrenheit - 32) * 5 / 9)
    elif menu == 2:
        celsius = int(input("Input Celsius : "))
        print((celsius * 9/5) + 32)
    elif menu == 3:
        number = int(input("Input number : "))
        decision = True
        if number < 2:
            print(f'{number} is NOT a prime number')
        else:
            for i in range(2, number):
                if number % i == 0:
                    decision = False
                    break
        if decision:
            print(f"{number} is a prime number")
        else :
            print(f"{number} is NOT a prime number")
    elif menu == 4:
        numbers = input("Input first second number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        if n1 > n2:
            n1, n2 = n2, n1

        for j in range(n1, n2+1):
            decision2 = True
            if j < 2:
                pass
            else:
                for k in range(2, j):
                    if j % k == 0:
                        decision2 = False
                        break
                if decision2:
                    print(j, end=' ')
    elif menu == 5:
        break
    else:
        print('Input only 1~5 integers')
        break