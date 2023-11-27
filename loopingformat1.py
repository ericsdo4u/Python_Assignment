score = float(input('enter scores:'))
total = 0
count = 0
whlie score != -1:
	total += score
	count += 1
average = total / count
print('the average score is', average)