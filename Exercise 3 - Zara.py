# Create a dictionary called brand which value is the information from part one (turn the info into keys and values)
brand = {
            'name': 'Zara',
            'creation_date': 1975,
            'creator_name': 'Amancio Ortega Gaona',
            'type_of_clothes': 'men, women, children, home',
            'international_competitors': 'Gap, H&M, Benetton',
            'number_stores': 7000,
            'major_color':{
                'France': 'blue',
                'Spain': 'red',
                'US': 'pink, green'
            }
    }
print(brand)
#Change the number of stores to 2.
brand['number_stores']= 2
print(brand)

#Print a sentence that explains who Zaras clients are.
print("Zara's clients are ", brand['type_of_clothes'])

#Add a key called country_creation with a value of Spain.
new_key = {'Country creation': 'Spain'}
brand.update(new_key)
print(brand)

#Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
for key, value in brand.items():
    if key == "international_competitors":
        print(key, "is present")
        #brand(international_competitors[4]) = "Desigual"
        brand.update(international_competitors="Gap, H&M, Benetton, Desigual")
        print(brand)
        break

#Delete the information about the date of creation.
del brand['creation_date']
print(brand)

#Print the last international competitor.
last_key = list(brand['international_competitors'])[-1]
print(last_key)

#Print the major clothes colors in the US.
print(brand['major_color'])

#Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))

#Print the keys of the dictionary.
for keys, value in brand.items():
        print(keys)

#Create another dictionary called more_on_zara with the following details:
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
    }

#Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand["new_dict"] = more_on_zara
print(brand)

#Print the value of the key number_stores. What just happened ?
print(brand['number_stores'])