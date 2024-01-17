# t1 = (5)
# t2 = 5,
# t3 = (5,)
# t4 = (5, 7)
# t5 = 5, 7
# print(type(t1), type(t2), type(t3), type(t4), type(t5))
# # , 기호를 포함하면 tuple 형태가 된다.
# t6 = "python", "kim"    # packing
# print(type(t6), t6[1])
# subject, prof = t6      # unpacking
# print(prof)
# print(subject)
# # a, b, c =t6 ValueError: not enough values to unpack (expected 3, got 2)
# t7 = ()         # 빈 튜플
# t8 = tuple()    # 빈 튜플
# print(type(t7), type(t8))
# t9 = 1, 2, 3
# t10 = 1, 2, 4
# print(t9 == t10, t9 < t10, t9 > t10)        # 대수 비교시 순서대로 비교하므로 빠른 순서가 더 크면 큰값이다.
# # t11 = 4.43,
# # t12 = 3.97, 4.1, 3.27
# # print(id(t11))
# # t11 = t11 + t12  # t11 += t12
# # print(id(t11))    # 원래있던 자료가 바뀌는 것이 아니다. 주소가 바뀐것 뿐
# # split() : 문자열을 리스트로 구분해서 저장해줌
# A = 'a/b//c/d///e'
# print(A.split('/'))
# subjects = ["데이터베이스", "C++", "5", "Java", "Python", "Java", "9", "리눅스"]
# print(subjects[::-1])
# # subject[::-1]     원본은 안바뀜
# # subjects.reverse()   # 원본이 바뀜
# print(subjects)
# # subject.remove("Java")       동일한 값이 있는 경우 앞선 순서를 지운다.
# # del subjects[2]
# # subjects.pop(2)
# # pop()       #후입선출 시 유리
# # clear() 전부삭제     index() 오프셋 찾기      in *안에 있는지 확인*  count() 갯수 세기   join() 문자열로 만들어주기 짝찌로 split()
# # sort() 정렬 알파벳 순 오름차순 등 원본 바꿈      sorted() 사본을 저장함
# # subjects.sort(reverse=True)   # => desc 내림차순            #reverse=False가 기본값
# copy_subjects = sorted(subjects)
# print(subjects)
# print(copy_subjects)
# # len() 원소 갯수
# 참조개념(얕은 복사)       깊은 복사
import  copy
# subjects = ["a", "b", "c"]
subjects = ["a", ["b", "c"], "d"]
a = subjects
b = subjects.copy()
c = list(subjects)
d = subjects[:]
e = copy.deepcopy(a)        #deepcopy는 완전히 분리된 메모리 할당함
print(a, b, c, d, e)
subjects[1][1] = "x"
print(a,  b, c, d, e)
# shallow copy를 할 때 immutable 값들은 바뀌지 않지만 mutable 값들은 변한다.
# zip() 여러 시퀀스를 병렬로 순회(묶음)  제일 작은 원소갯수 기준
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list(zip(english, french)))
print(dict(zip(english, french)))
# 리스트 컴프리헨션
number_list = [number for number in range(1,6)]
print(number_list)