guess_me = 7
number = 1
while number <= guess_me+1:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
    elif number > guess_me:
        print('oops')
    number += 1