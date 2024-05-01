# modelo = folder // restaurant = file // Restaurant == class
from modelos.restaurant import Restaurant

restaurant_square = Restaurant('Square','Gourmet')
restaurant_mexican = Restaurant('Mexican Food', 'Mecican')
restaurant_japan = Restaurant('Japa','Japan')

restaurant_mexican.change_state()


def main():
	Restaurant.list_restaurants()

if __name__ == '__main__':
	main()
