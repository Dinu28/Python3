#Continue,break,pass in loops

a = 5
while (a>0):
	print(a,":Loop!")
	a=a-1
	
##########################
a = 5
while (a>0):
	if(a==3):
		a=a-1
		continue
	print(a,":Loop!")
	a=a-1

##########################
a = 5
while (a>0):
	if(a==3):
		a=a-1
		continue
	else:
		print(a,":Loop!")
		a=a-1
	
##########################
a = 5
while (a>0):
	if(a==3):
		break
	print(a,":Loop!")
	a=a-1
##########################
a = 5
while (a>0):
        if(a==3):
                a=a-1
                pass
        print(a,":Loop!")
        a=a-1

##########################
#Factorial of a number

num = input("Enter the number to find Factorial !")
result = 1
while ( num >=1):
	if(num ==1):
		break
	result = result * num
	num = num - 1
print result	

##########################
#Factorial of a number

num = input("Enter the number to find Factorial !")
result = 1
for num in range (1,num+1):
        result = result * num
        num = num - 1
print result
