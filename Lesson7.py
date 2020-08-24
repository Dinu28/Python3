#function()

def sum(a,b):
	result = a+b
	return result

c=sum(10,20)
print c

###################################
global num1 
num1= 40
def sum(num1,num2):
	result=num1+num2
	return result

num3=sum(num1,30)
print num3
