class Restaurant:
	name = ''
	category = ''
	active = False

restaurant_square = Restaurant()
restaurant_square.category = 'Italian'
restaurant_square.name = 'Bistro'

restaurant_pizza = Restaurant()
restaurant_pizza.name = 'Pizza Place'
restaurant_pizza.category = 'Fast Food'
restaurant_pizza.active = True

if restaurant_square.active == False:
	status = 'Not Active'
else:
	status = 'Active'

if restaurant_pizza.category == 'Fast Food':
	true_category = 'yes'
else:
	true_category = 'no'

print(f'Restaurant name: {restaurant_square.name}, Category: {restaurant_square.category}, Status: {status}')
print(f'\nRestaurant name: {restaurant_pizza.name}, Category: {restaurant_pizza.category}, Status: {restaurant_pizza.active}')
print(f'\nThe category is Fast Food: {true_category}')

category = Restaurant.category = ''

print(f'\nName of category is: {category}')
