class Restaurant:
	restaurants = []

	def __init__(self, name, category): #initialize
		self.name = name.title()
		self.category = category.upper()
		self._active = False
		Restaurant.restaurants.append(self)

	def __str__(self):
		return f'{self.name} | {self.category}'
	@classmethod
	def list_restaurants(cls):
		print(f'{'Restaurant Name'.ljust(25)} | {'Category Name'.ljust(25)} | {'Active?'}')
		for restaurant in cls.restaurants:
			print(f'{restaurant.name.ljust(25)} | {restaurant.category.ljust(25)} | {restaurant.active}')

	@property
	def active(self):
		return '⌧' if self._active else '☐'
	
	def change_state(self):
		self._active = not self._active
