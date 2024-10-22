#!python3

'''
##### Task 8
Read through the file **example2.py** for information on using the math module.
Calculate the length of a hypotenuse given 2 variables
Set the value of a to 5
Set the value of b to 8

Determine the length of the hypotenuse and store it into a variable called c
print the value of c

You may use either the ** operator or math.pow(x,y) for your exponents
You may use either math.sqrt(x) or the exponent to the power of 0.5 for your square root

 '''

a = float(5)
b = float(8)
c = float()


c = a**2 + b**2
c= c**0.5

print(c)