class Car:
	model = ''
	color = ''
	year = ''

my_car = Car()
my_car.model = 'Argo'
my_car.color = 'Red'
my_car.year = '2019'

print(f'{my_car.model} | {my_car.color} | {my_car.year}')


class Restaurant:
	def __init__(self, name, category):
		self.name = name
		self.category = category
	city = ''
	address = ''
	active = False

	def __str__(self):
		return f'{self.name} | {self.category}'


my_restaurant = Restaurant('Frank Restaurant', 'English Restaurant')
# my_restaurant.name = 'Frank Restaurant'
# my_restaurant.category = 'English Restaurant'
my_restaurant.city = 'Sao Paulo'
my_restaurant.address = 'Paulista, SP'

# print(f'{my_restaurant.name} | {my_restaurant.category} | {my_restaurant.city} | {my_restaurant.address}')

print(my_restaurant)


class Customer:
	def __init__(self, firstname, lastname, phone, city):
		self.firstname = firstname
		self.lastname = lastname
		self.phone = phone
		self.city = city
	def __str__(self):
		return f'{self.firstname} | {self.lastname} | {self.phone} | {self.city}'

frank_ltda = Customer('Frank', 'Bruno', '1199999-99999', 'Sao Paulo')

print(frank_ltda)
