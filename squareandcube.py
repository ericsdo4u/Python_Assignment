number0 = int(input('Enter integer number: '))

number1 = int(input('Enter integer number: '))

number2 = int(input('Enter integer number: '))

number3 = int(input('Enter integer number: '))

number4 = int(input('Enter integer number: '))

number5 = int(input('Enter integer number: '))

#print('		number	  square		cube' )
	
print(f"\t\tnumber\t\tsquare\t\tcube")

result0 = number0 * number0 
result2 = number0 * number0 * number0
		
print(f"\t\t{number0}\t\t{result0}\t\t{result2}")


result1 = number1 * number1
print("		1	", result1)

result22 = number2 * number2
print(f"\t\t{number2}\t\t{result22}\t\t{result22 * number2}")

result3 = number3 * number3
print("		3	", result3)

result4 = number4 * number4
print("		4	", result4)

result5 = number5 * number5
print("		5	", result5)


print(f"\t\tnumber\t\tsquare\t\tcube")

for num in range(5):
	print(f"\t\t{num}\t\t{num*num}\t\t{num*num*num}")

print(f"\t\tnumber\t\tsquare\t\tcube")
numbers = 1
while numbers <= 5:
	print(f"\t\t{numbers}\t\t{numbers * numbers}\t\t{numbers* numbers* numbers}")
	numbers +=1
