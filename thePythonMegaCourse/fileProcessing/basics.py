# how to read a file in python

#myfile = open("fruits.txt")
#content = myfile.read() # can be stored as a variable
#myfile.close() # this closes the file, good practice to close it
#print(myfile.read())

# better way to perform the above

#with open("fruits.txt") as myfile: # the close method will automatically close the file
#  content = myfile.read()
#
#print(content)

# create a file

#with open("vegetables.txt", "w") as myfile:
#  myfile.write("Tomato\nCucumber\nOnion")
#  myfile.write("\nGarlic")

# append to the existing list

with open("fruits.txt", "a+") as myfile: # open the file, append and open for reading and writing with "+"
  myfile.write("\nOkra")
  myfile.seek(0) # this sets the cursor back up to the top. if not it will stay at the bottom and if you print, it will print everything at the bottom which can be blank
  content = myfile.read()

print(content)