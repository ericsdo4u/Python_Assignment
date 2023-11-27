price = int(input('whats the car price: '))

if price < 10000000:
	print( price * 0.10, 'is road tax')

elif 	price >= 10000000 and price <= 30000000:
		print(price * 0.15, 'is road tax')
