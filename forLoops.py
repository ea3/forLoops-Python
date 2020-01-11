my_List = ['Emilio', 'Laura', 'Andrea', 'Tony', 'Ramon']
for name in my_List:
	print (name)

my_second_list = [1,2,3,4,5,6,7,8,9,10]
for number in my_second_list:
	if (number % 2 == 0 ): 			# check for even. 
		print(number)				#Prints multiple of 2. 
	else:
		print('Not an even number: {}'.format(number))
list_sum = 0

for number in my_second_list:
	list_sum = list_sum + number
print(list_sum)

myString = 'Hello World, My name is Emilio!'

for letter in myString:
	print(letter)

tup = (1,2,3)

for item in tup:
	print (item)

	#tuple unpacking

my_third_list= [(1,2),(3,4), (5,6), (7,8)]
print(len(my_third_list))


for (a,b) in my_third_list:
	print(a)
	print(b)

my_last_list = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in my_last_list:
	print (a)
	print(b)





print('##############################')
dictionary = {'k1':1, 'k2':2, 'k3':3}

for value in dictionary.values():
	print(value)





















