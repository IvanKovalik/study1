class Person:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def check(self):
        if self.name == '' or self.email == '' or self.age == 0:
            raise ValueError('You must provide a name, age and email')


def main():
    p = Person('name', 0, '')
    print(p.check())


main()
