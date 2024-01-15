# print("Hello Python~")
# univ = "Inha university"
# print(univ)
# print(univ[5])
# # univ[5] = 'U' // immutable
# # print(univ)
# subjects = ['python', 'c++', 'linux', 'data structure', 'database']
# print(subjects)
# print(subjects[3])
# subjects[3] = 'data structure & algorithm'  # mutable
# print(subjects)

# literal 설명 시 97 = 71 오류 사용
# flase = 123      reserved words
# 9test = 71
# isinstance

artists = ['BTS', '뉴진스', '핑클', 'HOT']
groups = artists
print(artists, groups)
artists[2] = 'seventeen'
print(artists, groups)
# 복제가 아니라 '참조'함을 알아야함

# f-string
# print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {pow(base_number , exponent_number)}')

# format function
# print('밑은 {0}, 지수는 {1} 결과 값은 {2}'.format(*args:base_number, exponent_number , pow(base_number , exponent_number)))
# 순서 안적어도 알아서 순서를 결정함

# c like
# print('밑은 %d, 지수는 %d, 결과 값은 %d' %(base_number, exponent_number, pow(base_number, exponent_number)))

# base_number = int(input('Input base numebr : '))
# exponent_number = int(input('Input exponent number : '))

# first_number = int(input("first number : "))
# second_number = int(input("second number : "))
# quotient = first_number // second_number
# remainder = first_number % second_number
# print(f'몫은 {quotient} 나머지는 {remainder}')

# first_number = int(input("first number : "))
# second_number = int(input("second number : "))
# print(f'몫은 {divmod(first_number, second_number)[0]} 나머지는 {divmod(first_number, second_number)[1]}')

dec = 65
octal = 0o101
hexadeciaml = 0x41
binary = 0b01000001
print(dec, octal, hexadeciaml, binary)
print(chr(binary), chr(octal), chr(hexadeciaml), chr(binary))      #ASCII code를 문자로 바꿔줌
# bin , oct , hex 진법별 함수 존재
# chr : ASCII -> 문자     ord : 문자 -> ASCII
print(ord("B"), ord('Z'), ord('a'), ord('2'))   #66, 90, 97, 50

# (100°F − 32) × 5/9 = 37.778°C
fahrenheit = float(input("Input Fahrenheit : "))
print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32)*5/9):.2f}C')