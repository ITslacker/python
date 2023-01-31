#colors = [11, 34, 98, 43, 45, 54, 54]

#for color in colors:
#  if color > 50:
#    print(color)

#colors = [11, 34.1, 98.2, "bob", 45.1, "tate", 54]
#
#for color in colors:
#  if isinstance(color,str):
#    print(color)

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color,int) and color > 50:
        print(color)