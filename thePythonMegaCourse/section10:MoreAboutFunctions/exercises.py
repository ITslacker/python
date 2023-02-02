#def bali(*args):
#    return sum(args) / len(args)
#    
#print(bali(10,20,30))

"""
Define a function that takes an indefinite number of strings as parameters and returns a list containing all the strings in UPPERCASE and sorted alphabetically. For example, if I called your function with foo("snow", "glacier", "iceberg") it should return ["GLACIER", "ICEBERG", "SNOW"].
"""

#def bali(*args):
#  args = [x.upper() for x in args]
#  return sorted(args)
#
#print(bali("snow", "glacier", "iceberg"))

def bali(*args): # define function
  steven = []  # prepare an empty list
  for x in args:
    steven.append(x.upper()) # append the uppercase words
  return sorted(steven) # get the results

print(bali("eat", "bark", "dance"))

"""
Enter the correct parameters inside find_sum() so that the output of the code is 9.

def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum())
"""

def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a = 5, b = 4))