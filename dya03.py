subjects = "pythoncdatabaselinux"
print(subjects.isalnum())
subject = input("수강긴청과목 입력 : ")
try :
    print(f'해당 과목이 존재합니다. 위치는 {subjects.index(subject)}번 인덱스입니다.')
except ValueError :
    print('해당 과목이 존재하지 않습니다.')
#count 함수 -> 갯수 세는 옵션
# is가 붙는 애들은 True, False (Boolean값) 배출
# 대소문자 관련 함수들
# 배열, 포맷팅
print('%e' %0.7045)
# 포맷팅 지정 시 기본값(+)은 오른쪽정렬
# %s %f %d {}   {}.format(thing)        'The {1} is in the {0}.'.format(thing, place)   번호 지정가능 없으면 차례대로
# dic 사용 가능