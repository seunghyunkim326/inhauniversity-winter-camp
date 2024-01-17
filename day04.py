# squares = []
# for i in range(1,6):
#     squares.append(i*i)
# print(squares)

# list comprehension
# squares = [i*i for i in range(1,6)]
# print(squares)
# numbers = [i for i in range(1,6) if i % 2 == 1]
# print(numbers)

even_squares = [i*i for i in range(1,6) if i % 2 == 0]
print(even_squares)