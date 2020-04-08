import math

def promien(a=0, b=0, x=0, y=0):
    return math.sqrt((x-a)**2 + (y-b)**2)
    

print("Promien wynosi: " + str(promien(1, 3, 4, 5)))
print("Promien wynosi: " + str(promien(a=1, b=3)))