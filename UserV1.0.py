class User:
    def __init__(self, first_name, last_name, age, gender):
        self.name = first_name
        self.surname = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f'This is {self.surname.title()} {self.name.title()}.', end=' ')
        if self.gender == 'male':
            print(f'He is {self.age}.')
        else:
            print(f'She is {self.age}.')

    def greet_user(self):
        print(f'Hello, {self.name.title()}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


u1 = User('alice', 'watson', 25, 'female')
u2 = User('alex', 'lawrence', 25, 'male')

# u1.describe_user()
# u1.greet_user()

u2.describe_user()
# u2.greet_user()
u2.increment_login_attempts()
u2.increment_login_attempts()
u2.increment_login_attempts()
u2.increment_login_attempts()
print(f'Login attempts to {u2.name.title()} profile: {u2.login_attempts}')
u2.reset_login_attempts()
print(f'History was cleaned up. Login attempts turned {u2.login_attempts}')
