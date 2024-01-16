# subjects = {'python' : 'kim', 'c++' : 'sung', 'data structure' : 'kim', 'database' : 'kang'}
# print("{0[python]} {0[data structure]}".format(subjects))
# break 가장 가까운 반복문 탈출
# continue 아래 내용 무시하고 가까운 반복문 다시 돌림
# 소수 판별기 만들어보기
# number = int(input())
# count = 0
# for _ in range(number) :
#     \


number = int(input("Input number : "))
is_prime = True # int -> bool
i = 2
if number < 2 :
    print(f'{number} is NOT prime number!')
else :
    while i < number:
        if number % i == 0 :
            is_prime = False    # remove +
            break       # break를 통해서 시간, 불필요 계산을 줄일 수 있음
            #print(i, end=' ')
        i += 1
    # if cnt == 0 :
    if is_prime:    # remove ==
        print(f'{number} is prime number')
    else :
        print(f'{number} is NOT prime number!')