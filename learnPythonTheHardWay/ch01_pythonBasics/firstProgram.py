# This program says hellow and asks for my name

print('Hello, world!')
# ask for their name
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
# ask for their age
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')