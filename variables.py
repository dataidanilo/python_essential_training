# test some variables and basic functions
"""
this is an alternative
if I need more lines
to explain something in a comment
"""
# variables
x = 5
y = "it's greater"
Y = 'it is greater' # Variable name is case sensitive, it works also with single quote
z = str(3) # if i want to assign data type, in this case is string

# variables data type
print(type(x))
print(type(y))

# multiple variables
a, b, c = "first", "second", "third"
A = B = C = "same value to multiple variables"
# unpack -> extract values in variables
values = ["first", "second", "third"]
a, b, c = values

# print options
print(a,b,c)
print(a+b+c)
a = 1
b = 1
c = 1
print (a+b+c) # works as mathematical operator,it doesn't works with strings and numerical var together

if (5 > 2):
    print(y)
    print("it's not greater")


# global and local variables
myVar = "global"
def myFunction():
    myVar = "local" # this is a local variable, it doesn't change the global one
    print("This is a "+myVar+" variable")

myFunction()

print(myVar)

# cast
x = int(2.8) # it returns 2
y = float(2) # it returns 2.0
z = str(2)   # it return '2'
print(x)
print(y)
print(z)

# multiline variable
a = """ this is
my multiline
variable """
 
