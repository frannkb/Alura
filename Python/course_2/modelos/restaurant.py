from modelos.avaliation import Avaliation

class Restaurant:
	restaurants = []

	def __init__(self, name, category): #initialize
		self.name = name.title()
		self.category = category.upper()
		self._active = False
		self._avaliation = []
		Restaurant.restaurants.append(self)

	def __str__(self):
		return f'{self.name} | {self.category}'
	@classmethod
	def list_restaurants(cls):
		print(f'{'Restaurant Name'.ljust(25)} | {'Category Name'.ljust(25)} | {'Avaliation'.ljust(25)} | {'Active?'.ljust(25)}')
		for restaurant in cls.restaurants:
			print(f'{restaurant.name.ljust(25)} | {restaurant.category.ljust(25)} | {str(restaurant.avaliation_average).ljust(25)} | {restaurant.active.ljust(25)} ')

	@property
	def active(self):
		return '⌧' if self._active else '☐'
	
	def change_state(self):
		self._active = not self._active
	
	def get_avaliation(self, customer, grade):
		avaliation = Avaliation(customer, grade)
		self._avaliation.append(avaliation)

	#add the property to retrieve the information stored in the method
	@property
	def avaliation_average(self):
		#check if there is some value in list avaliation[] if not return 0
		if not self._avaliation:
			return 0
		#sum total of value in avaliation[]
		sum_grades = sum(avaliation._grade for avaliation in self._avaliation)
		#check total of avaliation 
		total_grades = len(self._avaliation)
		#get the average and return a floating-point value with the function 'round' like the grade 4.0
		average = round(sum_grades / total_grades, 1)
		return average
