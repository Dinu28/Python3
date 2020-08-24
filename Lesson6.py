#list[] - Array
#touple () - Readonly
#dictionary {"1":"Square","name":"RAM".....}, can have mixed types

a=[10,20,30,40]
print(a[0],a[2])
print a[1],a[3]
print max(a)
print min(a)
##########################

a=[10,20,"Hi",40,54,'HELLO',33,67]
i=0
while(i<len(a)):
	print a[i]
	i=i+1

###################################

a=(5,'' ,"Hi",40,54,'HELLO',33,67)
i=0
while(i<len(a)):
        print a[i]
        i=i+1

###################################

a={"name":'DEN',"age":25}
print a["name"]
print a["age"]

##################################
a=["apple","grapes"]
b=("apple","grapes")
print a
print b

###################################
a=["apple","grapes"]
#b=("apple","grapes")
print a
a.append("banana")
print a
a.insert(1,"kiwi")
print a

###################################
#a=["apple","grapes"]
b=("apple","grapes")
print b
a.append("banana")
print b
a.insert(1,"kiwi")
print b

###################################
c={1:"Hello",2:"World!"}
print(c)
print c[1]
c.clear()
print c

##################################
a=[]
while(True):
	val=input("Enter a number");
	if(val == -1):
		break;	
	else:
		a.append(val)
print a

##################################
a=[]
counter = 0
while (True):
		a.append(input())
		if(a[counter] == -1):
			break
		else:
			counter=counter+1
for x in a:
	print(x)
