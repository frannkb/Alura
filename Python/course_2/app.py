# modelo = folder // restaurant = file // Restaurant == class
from modelos.restaurant import Restaurant

restaurant_square = Restaurant('Square','Gourmet')
restaurant_square.get_avaliation('Frank', 8)
restaurant_square.get_avaliation('Bruna', 4)

def main():
	Restaurant.list_restaurants()

if __name__ == '__main__':
	main()
