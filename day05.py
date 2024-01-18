# prime number
def isprime(n):
    if n < 2:
        return False
    else:
        i = 2
        while i**2 <= n:
            if n % i == 0:
                return False
            i += 1
        return True

n1, n2 = map(int, input("Input first second number : ").split())

if n1 > n2:
    n1, n2 = n2, n1

for number in range(n1, n2+1):
    if isprime(number):
        print(number, end=' ')