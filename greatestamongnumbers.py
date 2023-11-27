num1 = int(input('whats the car price: '))
num2 = int(input('whats the car price: '))
num3 = int(input('whats the car price: '))

if num1 > num2:
	if num1 > num3:
		print(num1, 'is the greatest')

if num2 > num1:
	if num2 > num3:
		print(num2, 'is the greatest')

if num3 > num1:
	if num3 > num2:
		print(num3, 'is the greatest')