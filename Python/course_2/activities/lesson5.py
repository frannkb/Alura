class AccountBank:
	accounts = []
	def __init__(self, titleholder, balance):
		self.titleholder = titleholder
		self.balance = float(balance)
		self.active = False
		AccountBank.accounts.append(self)

	def __str__(self):
		return f'This account belongs to: {self.titleholder} and its balance is: {self.balance}'

	@classmethod
	def list_account(show):
		print(f'{'Account name'.ljust(20)} | {'Balance'.ljust(20)} | {'Active?'}')
		for account in show.accounts:
			print(f'{account.titleholder.ljust(20)} | {str(account.balance).ljust(20)} | {account.active}')

	# @property
	# def is_active(self):
	# 	return print(f'your account is active!') if self.active else print(f'your account is not active!')

	# def activate_account(self):
	# 	self.active = not self.active

frank = AccountBank('frank', 1114.12)

AccountBank.list_account()
