class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        self.email = email
Ted = EmailPerson('Ted', 'Ted@gmail.com')
print(Ted.name, Ted.email)
# 왜 안될까?