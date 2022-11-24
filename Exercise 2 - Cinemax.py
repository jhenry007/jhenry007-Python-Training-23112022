family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

result = []
dollar_to_pay = 0

for key, value in family.items():
	print(value)
	if value < 3 :
		print("Free of charge")
		dollar_to_pay = 0
		result.append(dollar_to_pay)
	elif value >= 3 and value < 12:
		print("$10 dollar to pay")
		dollar_to_pay = 10
		result.append(dollar_to_pay)
	elif value >= 12:
		print("$15 dollar to pay")
		dollar_to_pay = 15
		result.append(dollar_to_pay)

print(result)
Sum = sum(result)
print("Total amount to pay is $", Sum)
#------------------------------------------------

#Bonus: Ask the user to input the names and ages instead of using the provided family
#variable (Hint: ask the user for names and ages and add them into a family dictionary
#that is initially empty).

family_2 = {}
for i in range(3):
    name = input("Insert your name here : ")
    age = input("Insert your age here : ")
    family_2[name] = age
print(family_2)