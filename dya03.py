subjects = {'python' : 'kim', 'c++' : 'sung', 'data structure' : 'kim', 'database' : 'kang'}
print("{0[python]} {0[data structure]}".format(subjects))
# break 가장 가까운 반복문 탈출
# continue 아래 내용 무시하고 가까운 반복문 다시 돌림
# 소수 판별기 만들어보기
# number = int(input())
# count = 0
# for _ in range(number) :
#     \


number = int(input("Input number : "))
cnt = 0
i = 2
while i < number:
    if number % i == 0 :
        cnt += 1
    i += 1
if cnt == 0:
    print(f'{number} is prime number')
else :
    print(f'{number} is NOT prime number!')