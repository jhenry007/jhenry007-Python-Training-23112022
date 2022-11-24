users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

#>>> print(disney_users_A)
#{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
new_list = []
for (index, item) in enumerate(users):
	elem = str(item) + " : " + str(index)  # str() converts items to strings so they can be joined
	new_list.append(elem)
print(new_list)

#>>> print(disney_users_B)
#{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
new_list1 = []
for (index1, item1) in enumerate(users):
	elem1 = str(index1) + ": " + str(item1) # str() converts items to strings so they can be joined
	new_list1.append(elem1)
print(new_list1)

#>>> print(disney_users_C)
#{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
users.sort()
print(users)

new_list2 = []
for (index2, item2) in enumerate(users):
	elem2 = str(item2) + " : " + str(index2)  # str() converts items to strings so they can be joined
	new_list2.append(elem2)
print(new_list2)



print(new_list3)