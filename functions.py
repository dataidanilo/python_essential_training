
#=================================
#            FUNCTIONS
#=================================

def myFunction():
    print('this is my funtion')

def myName(Name, Surname):
    print('My name is ' + Name + ' ' + Surname)
myName('Danilo', 'Cassatella')

# unknown arguments
def favAnimals(*animals):
    print('I love animals, for example i like ' + animals[0])
favAnimals("pandas", "dogs", "horse", "cats")

# unknown keyword arguments
def myPet(**pet):
    print('My pet is a ' + pet["animal"])
myPet(animal = "dog", name = "Rex")

# default value
def myPet(pet = 'dog'):
    print('My pet is a ' + pet)
myPet('cat')
myPet()
myPet('rabbit')

# list as argument
def myLunch(food):
    for x in food:
        print(x)
todayLunch = ['pasta', 'salad', 'fruits']
myLunch(todayLunch)

def mySum(x):
    return 6 + x
mySum(3)

# only positional argument
def mySum(x, /):
    return 6 + x
print(mySum(3))

# only keyword argument
def mySum(*, x):
    return 6 + x
print(mySum(x = 3))

# combine  types
# before / only positional
# after * only keyword
def mySum(a, b, /, *, c, d):
    print(a + b + c + d)
mySum(1, 3, c = 4, d = 8)

def myRecursion(k):
    if(k > 0):
        result = k 
        myRecursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nThis is my recursion")
myRecursion(5)

# lambda function
def myMulti(n):
    return lambda a : a * n
myDouble = myMulti(2)
myTriple = myMulti(3)

print(myDouble(7))
print(myTriple(7))
