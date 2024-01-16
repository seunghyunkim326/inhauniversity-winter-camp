number = int(input("Input number : "))
is_prime = True  # int -> bool
i = 2
if number < 2:
    print(f'{number} is NOT prime number!')
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    # if cnt == 0 :
    if is_prime:    # remove ==
            print(f'{number} is prime number')
    else :
            print(f'{number} is NOT prime number!')
# assignment : 더 보완할 것을 찾는 것
# sequence type : 순서를 가지는 값들        for in 구문에서 sequence type 사용가능
# else 가 for 문과 짝이 될 수 있다!!
# range()는 generator는 메모리에 저장 X     for문 감소형식 및 계단형식으로 사용 가능
