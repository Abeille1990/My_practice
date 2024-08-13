class User:
    def __init__(self, first_name, last_name, age, gender):
        self.name = first_name
        self.surname = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f'This is {self.surname.title()} {self.name.title()}.', end = ' ')
        if self.gender == 'male':
            print(f'He is {self.age}.')
        else:
            print(f'She is {self.age}.')

    def greet_user(self):
        print(f'Hello, {self.name.title()}')


u1 = User('alice', 'watson', 25, 'female')
u2 = User('alex', 'lawrence', 25, 'male')

u1.describe_user()
u1.greet_user()

u2.describe_user()
u2.greet_user()
