'''All methods of list
	append
	count
	extend
	insert
	pop
	remove 
	reverse
	sort '''

# create list
lst = [41, 21, 3, 3, 34, 10, 9, 10, 56]

# Iterate the list
for i in lst:
    print(i)

# appending in list
lst.append(20)

# Lenght of string
print("Lenght is " + str(len(lst)))

print("Frequency of 3 is " + str(lst.count(3)))

# Sorting the list
lst.sort()

# pop the last element from list
lst.pop()

for i in lst:
    print(i)

# List Slicing
for i in lst[:4]:
    print(i)


