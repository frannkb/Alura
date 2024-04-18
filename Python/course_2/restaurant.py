class Restaurant:
	name = ''
	category = ''
	active = False

restaurant_square = Restaurant()
restaurant_square.name = ''
restaurant_square.category = 'Gourmet'

restaurant_pizza = Restaurant()

restaurants = [ restaurant_pizza, restaurant_square]

print(vars(restaurant_square))
