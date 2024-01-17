t1 = (5)
t2 = 5,
t3 = (5,)
t4 = (5, 7)
t5 = 5, 7
print(type(t1), type(t2), type(t3), type(t4), type(t5))
# , 기호를 포함하면 tuple 형태가 된다.
t6 = "python", "kim"    #packing
print(type(t6), t6[1])
subject, prof = t6      #unpacking
print(prof)
print(subject)
# a, b, c =t6 ValueError: not enough values to unpack (expected 3, got 2)
t7 = ()         #빈 튜플
t8 = tuple()    #빈 튜플
print(type(t7), type(t8))
t9 = 1, 2, 3
t10 = 1, 2, 4
print(t9 == t10, t9 < t10, t9 > t10)        # 대수 비교시 순서대로 비교하므로 빠른 순서가 더 크면 큰값이다.
# t11 = 4.43,
# t12 = 3.97, 4.1, 3.27
# print(id(t11))
# t11 = t11 + t12  # t11 += t12
# print(id(t11))    # 원래있던 자료가 바뀌는 것이 아니다. 주소가 바뀐것 뿐