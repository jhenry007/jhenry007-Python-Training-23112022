keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print("Original key list is : " + str(keys))
print("Original value list is : " + str(values))

# using naive method
# to convert lists to dictionary
res = {}
for key in keys:
	for value in values:
		res[key] = value
		values.remove(value)
		break

# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))