fruits =["banana","aappel","strawberry"]

#new_lst = []
#
#[print(fruit) for fruit in fruits]
#
#for fruit in fruits:
#	new_lst.append(fruit.upper())
#	print(new_lst)
#
#[print(new_lst) for fruit in fruits ]

new_list = [fruit.upper() for fruit in fruits]
print(new_list)


bits = [True,False,True,False,True,False,True,False,True,False,True,False,True,False,]
#new_bits = []
#
#for b in bits:
#	if b == True:
#		new_bits.append(1)
#	else:
#		new_bits.append(0)
#
#print(bits)
#print(new_bits)

super_bits = [1 if b == True else 0 for b in bits]
print(super_bits)

