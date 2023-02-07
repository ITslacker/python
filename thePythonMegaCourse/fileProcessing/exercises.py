# reading and processing text (E)
"""
Read the bear.txt file, and print out the first 90 characters of its content.
"""

#with open("bear.txt") as fileBear:
#  content = fileBear.read()
#print(content[:91])

"""
Define a function that gets a single string character and a filepath as parameters and returns the number of occurences of that character in the file.
"""

#def bear(character, filepath="bear.txt"):
#  fileBear = open(filepath)
#  content = fileBear.read()
#  return content.count(character)
#
#print(bear("o"))

"""
Use Python to create a file with name file.txt and write the text snail there.
"""

#with open("file.txt", "w") as myfile:
#  myfile.write("snail")

"""
Create a first.txt file that contains the first 90 characters of bear.txt.

Note that you should read the content of bear.txt with Python, extract its first 90 characters with Python, and write those characters in first.txt with Python.
"""

#with open("bear.txt") as bearFile:
#  content = bearFile.read()
#  with open("first.txt", "w") as firstFile:
#    firstFile.write(content[:90])

"""
Append the text of bear1.txt to bear2.txt. In other words, bear2.txt should contain its text and the text of bear1.txt after that.
"""
#with open("bear1.txt", "r") as bear1File:
#  bear1Content = bear1File.read()
#  with open("bear2.txt", "a+") as bear2File:
#    bear2File.write(bear1Content)
#    bear2Content = bear2File.read()
#
#print(bear2Content)

"""
The existing content of data.txt looks like this:

1.3, 1.5

2.3, 2.7

Use Python to modify the content of data.txt so that its content looks like below:

1.3, 1.5

2.3, 2.7

1.3, 1.5

2.3, 2.7

1.3, 1.5

2.3, 2.7

So, you need to find a way to insert the existing content two more times.
"""
with open("data.txt", "a+") as dataFile:
  dataFile.seek(0)
  content = dataFile.read()
  dataFile.seek(0)
  dataFile.write(content)
  dataFile.write(content)