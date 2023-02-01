#temps = [221, 234, 340, 230, -9999, -11]
#
#new_temps = [temp / 10 for temp in temps if temp != -9999]
#
#print(new_temps)

"""
Define a function that takes as parameter a list that contains both numbers and strings and returns the same list but with zeros instead of strings. For example, I called your function with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 0, 95, 94, 0].
"""
def foo(lst):
  return [i if not isinstance(i, str) else 0 for i in lst]

print(foo([99, 'no data', 95, 94, 'no data']))

"""
Define a function that takes as parameter a list that contains decimal numbers as strings and returns the sum of those numbers. For example, I called your function with foo(['1.2', '2.6', '3.3']) it should return 7.1. Note that the floats of the input list are string datatypes.
"""

def foo(lst):
    return sum([float(i) for i in lst])

