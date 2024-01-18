# def squares(n):
#     return n * n
even_numbers = [i for i in range(101) if i % 2 == 0]
print(even_numbers)
# print(tuple(map(squares, even_numbers)))

# print(tuple(map(lambda x: x**2, even_numbers)))
Z = lambda x : x**2
print(tuple(map(Z, even_numbers)))