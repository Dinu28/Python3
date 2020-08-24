#!/usr/bin/env python
#File operations

###################################
#Find a word in the file

fil=open("test1.txt","r")
buff=fil.read()
word=raw_input("Enter a word to search:")
if(word in buff):
	print("Yes,Found it!")
else:
	print("Not Found!")

