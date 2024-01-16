course = "* KEB 2024# KEB !Bootcamp KEB...*!#"
# print(course)
# course = course.replace('KEB' , 'Inha' , 2)     #갯수도 설정 가능
# print(course)
# print(course.replace('KEB' , 'Inha'))   #.replace 값은 literal 값이다. 메모리값을 바꾸지 않는다.
# print(course)
# course = course.replace('KEB' , 'Inha') #메모리값 바꾸려면 재할당 필요
# print(course)
# print(course.strip())   #기본은 공란을 자름
# print(course.strip('!#.'))
# print(course.strip('.#!*'))     #연속된 것만 자름

print(course.find('KEB'))
print(course.rfind('KEB'))
print(course.index('KEB'))
print(course.rindex('KEB'))
print(course.find('Inha'))  # -1
print(course.index('Inha')) # ValueError : substring not found