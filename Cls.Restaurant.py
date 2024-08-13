class Restaurant():
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'\nRestaurant {self.name} serves {self.cuisine_type} cuisine.')

    def open_restaurant(self):
        print(f'{self.name} is open and waiting for you!')

r1 = Restaurant('Azimut', 'Georgian')
r2 = Restaurant('Balalayka', 'Russian')

print(r1.name)
print(r2.cuisine_type)
r1.describe_restaurant()
r1.open_restaurant()

r2.describe_restaurant()
r2.open_restaurant()