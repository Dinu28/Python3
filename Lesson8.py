#File operations

f=open("test.txt","w")
f.write("HOW ARE YOU YOU")
print("File name is:",f.name)
print("File mode is:",f.mode)
if(f.closed):
	print("YES")
else:
	print("NO")
print(f.closed)
f.close()
if(f.closed):
        print("YES")
else:
	print("NO")
print(f.closed)

#####################################

e=open("testw.txt","r")
pr=e.read(5)
print(e.read())
print pr
e.close()

###################################

x=open("test2.txt","w+")
x.write(raw_input())
x.close()

y=open("test2.txt","r")
print(y.read())
y.close()
