class people:
	def __init__(self, name= '', age=0 , profession=''):
		self.name = name
		self.age = age
		self.profession = profession

	def __str__(self):
		return f'{self.name} | {self.age} | {self.profession}'
	
	@property
	def hello(self):
		if self.profession:
			return f'Hello, I am {self.name}! I work in {self.profession}.'
		else:
			return f'Hello, I am {self.name}'
	
	def	birthday(self):
		self.age += 1

frank = people('frank', 32, 'IT')

frank.birthday()

print(frank)
print(frank.hello)
