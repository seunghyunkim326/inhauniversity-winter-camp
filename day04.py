numbers = input("Input first second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])
if n1 > n2:
    n1, n2 = n2, n1

for j in range(n1, n2+1):
    decision2 = True
    if j < 2:
        pass
    else:
        i = 2
        while i*i < n1:     #performance issue
            if n1 % i == 0:
                decision2 = False
                break
            i = i + 1
        #     print(i, end=' ')     #loop count
        if decision2:
            pass
            print(j, end=' ')