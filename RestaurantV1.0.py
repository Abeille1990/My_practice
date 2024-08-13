class Restaurant():
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.latest_served_count = 0

    def describe_restaurant(self):
        print(f'\nRestaurant {self.name} serves {self.cuisine_type} cuisine.')

    def open_restaurant(self):
        print(f'{self.name} is open and waiting for you!')

    def number_served_counter(self):
        print(f'Last year it served {self.number_served} clients.')

    def set_number_served(self, guests):
        self.number_served = guests

    def increment_number_served(self, new_guests):
        self.number_served += new_guests
        print(f'Since than the number of guests has increased to {self.number_served}!')

r1 = Restaurant('Azimut', 'Georgian',)
r2 = Restaurant('Balalayka', 'Russian')

print(r1.name)
print(r2.cuisine_type)
r1.describe_restaurant()
r1.open_restaurant()
# r1.number_served = 350
r1.set_number_served(300)
r1.number_served_counter()
r1.increment_number_served(800)

r2.describe_restaurant()
r2.open_restaurant()
# r2.number_served = 500
r2.set_number_served(1050)
r2.number_served_counter()
r1.increment_number_served(500)