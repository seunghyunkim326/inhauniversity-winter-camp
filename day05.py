# univ = 'inha university'
# counts = {x: univ.count(x) for x in univ}           # dictionary comprehension
# print(counts)

univ = 'inha university'
counts = dict()
for x in univ:
    counts[x] = univ.count(x)
print(counts)

# assignment ex 8.10
# squares = {i: i*i for i in range(10)}     #  i**2    pow(i, 2)
# print(squares)

squares = dict()
for i in range(10):
    squares[i] = i**2
print(squares)