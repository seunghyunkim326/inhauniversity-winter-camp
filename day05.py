# 9.16 연습문제 2)
# range(10)의 홀수를 반환하는 get_odds 제너레이터 함수 정의. for문으로 반환된 세번째 홀수 찾아 출력
# 제너레이터 => 이터레이터 직접 만들 때 사용하는 구문
# 함수내에 yield라는 키워드 포함 시 그 함수는 제너레이터가 됨
# next()함수를 통해서 제너레이터 실행
def get_odds():
    for i in range(10):
        if i % 2 == 1:
            yield i
A = get_odds()
for x in A:
    if x == 5:
        print(x)

# numbers = [1, 2, 3, 4, 5, 6]
# # print("::".join(numbers))
# print("::".join(map(str, numbers)))

# numbers = list(range(1,10+1))
#
# print(list(filter(lambda x: x%2==1,numbers)))
# print(list(filter(lambda y: y%2==0,numbers)))