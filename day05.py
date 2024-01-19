# def factorial_repetition(n) -> int:
#     """
#     반복문을 이용한 팩토리얼 함수
#     :param n: 정수
#     :return:
#     """
#     result = 1
#     for i in range(2, n+1):
#         result = result * i
#     return result
#
# def factorial_recursion(n):
#     """
#     재귀함수를 사용한 팩토리얼 함수
#     :param n: 정수 int
#     :return:  function, int
#     """
#     if n == 1:
#         return  n
#     else:
#         return n * factorial_recursion(n-1)
# number = int(input("number : "))
# print(factorial_recursion(number))
# print(factorial_repetition(number))
# print(globals())

import random
# numbers = list()
# for i in range(5):
#     numbers.append(random.randint(1, 100))
class OopsException(Exception):
    pass

numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

try:
    pick = int(input(f"Input index (0 ~ {len(numbers)-1}) : "))
    print(numbers[pick])
    raise OopsException("Oops~~")        # exception!
except IndexError as err:
    print(f"Out of range : Wrong index number\n{err}")
except ValueError as err:
    print(f'Input Only Number~\n{err}')
except ZeroDivisionError as err:
    print(f"The denominator cannot be 0.\n{err}")
except OopsException as err:
    print(f"Oops Oops {err}")
except Exception as err:
    print(f"Error occurs : {err}")       # exception 먼저 사용 시 모든 에러를 잡아버림
else:
    print(f"Program terminate")

# except Exception as err:
#     print(err)                  # err은 system이 던져주는 에러 메세지