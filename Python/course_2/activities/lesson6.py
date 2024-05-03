class Book:

	list=[]

	def __init__(self, title, author, year):
		self.title = title
		self.author = author
		self.year = year
		self.able = True
		Book.list.append(self)
	
	def __str__(self):
		return f'Author: {self.author.ljust(30)} title: {self.title.ljust(25)} year: {str(self.year).ljust(20)} | {self.able}'
	
	def to_borrow(self):
		self.able = not self.able
	
	@staticmethod
	def is_able(year_to_check):
		for book in Book.list:
			if str(book.year) == year_to_check:
				print(f'{book.title} | {book.author} | {book.year} | {book.able}')
			else:
				print("Book not found, please check another year.")
				break
