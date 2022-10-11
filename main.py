class Person:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def check(self):
        if self.name == '' or self.email == '' or self.age == 0:
            raise ValueError('You must provide a name, age and email')

    def is_adult(self):
        return self.age >= 18

    def check_email(self):
        return len(self.email) > 4 and self.email.count('@') == 1


def main():
    p = Person('name', 100, 'gj@dasd')
    print(p.check())
    print(p.is_adult())
    print(p.check_email())


main()
