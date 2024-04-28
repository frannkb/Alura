class AccountBank:
	accounts = []
	def __init__(self, titleholder, balance):
		self.titleholder = titleholder.upper()
		self.balance = float(balance)
		self.active = False
		AccountBank.accounts.append(self)

	# Getter
	@property
	def active(self):
		return self._active
	
	#Setter
	@active.setter
	def active(self, new_active):
		self._active = new_active


	def __str__(self):
		return f'This account belongs to: {self.titleholder} and its balance is: {self.balance}'

	@classmethod
	def list_account(show):
		print(' -- Account Bank')
		print(f'{'Account name'.ljust(20)} | {'Balance'.ljust(20)} | {'Active?'}')
		for account in show.accounts:
			print(f'{account.titleholder.ljust(20)} | {str(account.balance).ljust(20)} | {account._active}')
	
	def active_account(self):
		self._active = not self._active
	
class CustomerBank:
	clients = []
	def __init__(self, firstname, lastname, age, city, country):
		self.firstname = firstname.upper()
		self.lastname = lastname.upper()
		self.age = age
		self.city = city
		self.country = country
		CustomerBank.clients.append(self)
	
	def __str__(self):
		return f'Your fully name is: {self.firstname} {self.lastname} | {self.age} | {self.city} | {self.country}'
	
	@classmethod
	def list_customers(client):
		print(' -- Account Customers:')
		print(f'{'Name'.ljust(20)} | {'Last Name'.ljust(20)} | {'Age'.ljust(20)} | {'City'.ljust(20)} | {'Country'.ljust(20)}')
		for account in client.clients:
			print(f'{account.firstname.ljust(20)} | {account.lastname.ljust(20)} | {account.age.ljust(20)} | {account.city.ljust(20)} | {account.country.ljust(20)}')


accoun1 = AccountBank('frank', 1114.12)
account2 = AccountBank('Bruna', 2000.00)
account2.active_account()
AccountBank.list_account()

print('\n')

frank_account = CustomerBank('Frank','Teixeira', '32', 'Sao Paulo', '')
bruna_account = CustomerBank('Bruna','Teixeira', '28', 'Sao Paulo', 'Brazil')
CustomerBank.list_customers()
