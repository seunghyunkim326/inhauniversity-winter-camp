university = "Inha\nUniversity!"
# print(university)
# univ = r"Inha\nUniversity!"
# print(univ)     #raw string
# number1 = input("First number : ")
# number2 = input("Second number : ")

# slicing and .replace()    문자열 offset(번호가 있는 좌석이라고 생각)
# substring start to end-1 [a:b:c] -> a부터c까지 b만큼 건너뛰면서
print(university[:4])
print(university[:-11])
print(university[0:len(university)])
print(university[:16])
print(university[::2])