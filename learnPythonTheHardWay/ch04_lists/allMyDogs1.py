#print('Enter the name of dog 1:')
#dogName1 = input()
#print('Enter the name of dog 2:')
#dogName2 = input()
#print('Enter the name of dog 3:')
#dogName3 = input()
#print('Enter the name of dog 4:')
#dogName4 = input()
#print('Enter the name of dog 5:')
#dogName5 = input()
#print('Enter the name of dog 6:')
#dogName6 = input()
#print('The dog names are:')
#print(dogName1 + ' ' + dogName2 + ' ' + dogName3 + ' ' + dogName4 + ' ' + dogName5 + ' ' + dogName6)

## new and improved version

dogNames = []
while True:
    print('Enter the name of dog ' + str(len(dogNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    dogNames = dogNames + [name] #list concatenation
print('The dog names are:' )
for name in dogNames:
    print('  ' + name)