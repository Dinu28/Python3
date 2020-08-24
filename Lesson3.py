#IF-ELSE
#IF-ELIF-ELSE

a = True 
if (a):
	print("YES")
else:
	print("NO")

##############################
b = False
if (b):
        print("YES")
else:
        print("NO")

################################
c = 10
d =20
if (c==d):
        print("EQUAL")
else:
        print("NOT EQUAL")
##############################

if (c>=d):
        print("EQUAL")
else:
        print("NOT EQUAL")

###################################
e = int(input("Enter a value"))
if (e<5):
	print("YES")
else:
	print("NO")

##################################
f = input("Enter a value")
if (f<5):
        print("YES")
else:
        print("NO")

#######################################
#Program to find max of two given numbers

g = int(input("Enter First Value:"))
h = input("Enter second value:")
if(g>h):
	print("First Value is max",g)
elif(h>g):
	print("Second value is max",h)
else:
	print("Both are equal")
