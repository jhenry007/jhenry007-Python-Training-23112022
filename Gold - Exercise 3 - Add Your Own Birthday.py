#Add this new code: before asking the user to input a person’s name to look up,
# ask the user to add a new birthday:
database = {}
for i in range(1):
	your_name = input("Please insert your name here :")
	your_birthday = input("Please insert your date of birth here (format : YYYY/MM/DD) :")

database[your_name] = your_birthday
print(database)

for key, value in database.items():
        if key == your_name:
        	print("The date of birth of", key, "is", value)
