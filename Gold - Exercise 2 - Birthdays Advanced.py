#Before asking the user to input a person’s name print out all of the names in the dictionary.
birthday = {
			'Jeremie' : '1986/06/29',
			'Quincy' : '1989/05/19',
			'Matthew' : '2012/09/08',
			'Camille' : '2014/11/13',
			'Thais' : '2016/12/21'
			}

print("You can look up the birthdays of the people in the list!" ,birthday)

print(birthday)
inputbox = input("Please provide with someone's name :")

for key, value in birthday.items():
        if key == inputbox:
        	print("The date of birth of", key, "is", value)
		else:
			print("Sorry, we don't have ", inputbox, "details")