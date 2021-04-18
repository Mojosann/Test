# Christmas_tree Initial version
# print a tree

for i in range(15):
	if i <10 :
		print('\n'.join((20-i)*' '+'*'*(i+i+1)))
	else:
		print(' '*20+'*' for i in range(15))

 for i in range(15):
	if i <10 :
		print((20-i)*' '+'*'*(i+i+1))
	else:
		print(' '*20+'*' for i in range(15))


 for i in range(22):
        if i < 4 :
            print((20-i)*' '+'*'*(i+i+1))
        elif 3 < i < 10 :
            print((23-i)*' '+'*'*((2*i)-5))
        elif 9 < i < 17 :
            print((28-i)*' '+'*'*((2*i)-15))
        else:
            print(' '*20+'*')


for i in range(26):
        if i < 6 :
            print((20-i)*' '+'*'*(i+i+1))
        else i > 6:
            print((26-i)*' '+'*'*(i+i+1))


for a in range(3):
       for i in range(5):
           print((5-i)*' '+'*'*(i+i+1))
       else:
           print(' '*20+'*')
