numbers = input("Input first second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])


if n1 > n2 :
    n1, n2 = n2, n1

for number in range(n1 , n2+1):
    is_prime = True  # int -> bool
    if number < 2:
        pass
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime :
            print(number, end=' ')
# 어제 과제 화씨 섭씨 4번 메뉴 구간 소수판정 3번 메뉴 소수판정 5번 메뉴 탈출 + 연습문제 p.143 6.5 연습문제