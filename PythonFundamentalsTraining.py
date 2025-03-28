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
a = """this is
my multiline
variable"""

#=================================
#             STRINGS
#=================================

wordVar = "something"

print(wordVar[0]) # it returns the first letter

print(wordVar[:4]) 
print(wordVar[4:]) 
print(wordVar[-9:-5]) 

print(wordVar.upper())
print(wordVar.lower())
print(wordVar.split("t"))
print("  this is a text  ".strip())
print("this is a text".replace("text","sentence"))

for x in wordVar:
    print(x)

print(len(wordVar))

# check if t is in the word
print("t" in wordVar)

if "t" in wordVar:
    print("yes, it's present.")

# combine text and numbers or operations, instead of using format.
price = 20
txt = f"the price is {price/2:.2f} dollars, with a 20% discount"
print(txt)
txt = f"the price is {'expensive' if price > 20 else 'cheap'}"
print(txt)

age = "20"
name = "Anna"
introduction = "Her name is {0}, {0} is {1} years old."
print(introduction.format(name,age))
introduction = "Her name is {name}, {name} is {age} years old."
print(introduction.format(name = "Jane", age = "22"))

# escape characters
print("this is a \"test\".")
print("this is a test.\nthis is a test.\nthis is a test.")

# boolean
def myFunction(): 
    return True

if myFunction():
    print("Yes!")
else:
    print("No!")

#=================================
#             LISTS
#=================================

# items in a lists are ordered and duplicates are accepted

countries = ["China","Brazil","Italy","China","Japan"]
print(countries)
print(countries[2])
print(len(countries))
print(type(countries))
print(countries[2:])
print(countries[:2])
print(countries[2:3])
print(countries[-2])

if "Japan" in countries:
    print("Yes, Japan is one of the countries.")
else:
    print("No, Japan is not included in the countries list.")

countries[0] = "Taiwan"
print(countries)
countries[1:3] = ["France", "Switzerland"]
countries[1:2] = ["Denmark", "Latvia"]      # change the second country of the list with 2 countries
countries[3:5] = ["Italy"]                  # change 2 countries with one

countries.insert(2,'Australia')
countries.append("Canada")
africa = ["Botswana", "Algeria"]
countries.extend(africa)

countries.remove('Australia')      # in case of duplicates, only the first value will be deleted
countries.pop()                    # delete the last value of the list
countries.pop(2)
del countries[1]
del countries                      # delete the entire list
countries.clear()                  # empty the list

countries = ["China","Brazil","Italy","China","Japan"]

for x in countries:
    print(x)

for x in countries:
    if x == "China":
        print(x)

for x in range(len(countries)):
    if countries[x] == "China":
        print(x)

x = 0
while x < len(countries):
    print(countries[x])
    x = x + 1

[print(x) for x in countries]

newCountries = []
for x in countries:
    newCountries.append(x)
print(newCountries)

newCountries.clear()

for x in countries:
    if "l" in x:
     newCountries.append(x)
print(newCountries)

# list comprehension
newCountries = [x for x in countries if "l" in x]
newCountries = [x.upper() for x in countries if "l" in x]
numericList = [x * 100 for x in range(10) if x < 7 ]
print(numericList)

# list sorting
print(newCountries)
print(numericList)
newCountries.sort()
numericList.sort()
newCountries.sort(reverse = True)
numericList.sort(reverse = True)
newCountries.sort(key = str.lower)
newCountries.reverse()

# copy
newCountries = countries.copy() # it creates a copy, not a reference
newCountries = list(countries)
newCountries = countries[:]
print(newCountries)

# join
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

for x in b:
    a.append(x)
print(a)

a.extend(b)
print(a)

#=================================
#             TUPLE
#=================================
#tuples are ordered and unchangeable
countriesTuple = ('Canada','Italy','Japan')
print(countriesTuple)
print(len(countriesTuple))

# one time tuples need a comma after the item
# otherwise is recognized as a string variable
oneItemTuple = ('item',)
notTuple = ('item')
print(type(oneItemTuple))
print(type(notTuple))

# a tuple can contains different data types
mixTuple = ("abc",12,True)
print(type(mixTuple))

# tuple() method
methodTuple = tuple(("item1", "item2", "item3")) # double round-brakets are needed
print(methodTuple)

print(countriesTuple[0])  # first item
print(countriesTuple[-1]) # last item
print(countriesTuple[-2]) # second last item
print(countriesTuple[0:2])
print(countriesTuple[:2])
print(countriesTuple[1:])
print(countriesTuple[-3:-1])

if "Canada" in countriesTuple:
    print("Canada is in countriesTuple.")

# workaround to change items in a tuple
# convert tuple into a list, make changes and then convert it back
x = list(countriesTuple)
x[0] = "United States"
x.append("Australia", "France", "Bolivia")
countriesTuple = tuple(x)

# unpack tuple
myTuple = ["a","b","c","d","e"]
(varA,varB,varC,varD,varE) = myTuple
print(varA)
print(varB)
print(varC)
print(varD)
print(varE)
(varA,varB,*varC) = myTuple # * assign an array with the last 3 items to varC
print(varA)
print(varB)
print(varC)
(varA,*varB,varC) = myTuple # * assign an array with items that are not assigned to varA and varC (first and last items)
print(varA)
print(varB)
print(varC)

# join tuples
tuple1 = ("a","b")
tuple2 = ("c","d")
tuple3 = tuple1 + tuple2
tuple1 = tuple1*3
print(tuple3)
print(tuple1)

#=================================
#              SET
#=================================
# sets are used to store multiple items in a variable
# sets are unordered and unchangeable, but items can be removed or added

mySet = {"Orange", "Blue", "Red"}
print(mySet)

multipleSet = {"abc",1,True,0,False,3} # 0 and False are considered zthe same value, ad 1 and True
print(multipleSet)
print(len(multipleSet))
print(type(multipleSet))
myNewSet = set(("Yellow", "Green", "Pink")) # double-brackets needed
print(myNewSet)
print("Yellow" in myNewSet)
print("Green" not in myNewSet)
print("Red" in myNewSet)

myNewSet.remove("Yellow")
myNewSet.discard("Yellow")
myNewSet.pop() # delete a random item
myNewSet.clear() # empty the set
del myNewSet

for x in myNewSet:
    print(x)

# Join
set1 = {"Orange", "Blue", "Red"}
set2 = {"Black", "White"}
set3 = {"Grey", "Yellow", "Pink", "Violet", "Red"}

set4 = set1.union(set2)
set4 = set1 | set2
set5 = set1.union(set2,set3)
set5 = set1 | set2 | set3
tuple1 = ("Brown", "White")
set6 = set1.union(tuple1) # join a set with a tuple
print(set4)
print(set5)
print(set6)

set1.update(set2) # add items from set2
print(set1)

# Intersection
interSet = set1.intersection(set3)
interSet = set1 & set3
print(interSet)

# Difference
diffSet = set1.difference(set3)
diffSet = set1 - set3
print(diffSet)
diffSet = set1.symmetric_difference(set3) # keep not common items from both
set1.difference_update(set3) # return and update set1 with no items in common with set3

#=================================
#          DICTIONARIES
#=================================
# sets are used to store items in key:value pairs

song = {
    "song" : "Glory Days",
    "artist" : "Bruce Springsteen",
    "year" : 1985,
    "producers" : ["Jon Landau", "Chuck Plotkin", "Bruce Springsteen", "Steven Van Zandt"] # items can be of any data type
}
print(song)
print(song["artist"])
print(len(song))
print(type(song))

song2 = dict(song = "Song 2", artist = "Blur", year = 1997) # dict() method

# access items
artist = song["artist"]
artist = song.get("artist")
print(artist)

x = song.keys()
print(x)
song["album"] = "Born in the U.S.A."
print(x)
x = song.values()
print(x)
y = song.items() # it returns all items as tuples in a list
print(y)

if "artist" in song:
    print("Yes, artist is one of the keys")

# update and add
song2["song"] = "SONG 2"
song2["rating"] = 8
song2.update({"genre":"rock"})
print(song2)

# remove
song2.pop("rating")
song2.popitem() # remove last inserted item
del song2["rating"]
song2.clear()
del song2 # to delete song2 completely

# copy dictionary
songCopy = song.copy()
songCopy = dict(song)
print(songCopy)

# nested dictionary

playlist = {
    "song1" : {
        "artist" : "The Strokes",
        "song" : "Someday"
    },
    "song2" : {
        "artist" : "The Hives",
        "song" : "Hate To Say I Told You So"
    },
    "song3" : {
        "artist" : "The Beatles",
        "song" : "Something"
    }
}

print(playlist["song1"]["artist"])

for x, obj in playlist.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])


#=================================
#           IF...ELSE
#=================================

a = 10
b = 12

if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal b")
else:
    print("b is greater than a")

# short statement
print("Yes") if "hello".startswith("h") else print("No")
print("a is greater than b.") if a > b else print("a and b are equal.") if a == b else print("b is greater than a.")
print("true") if not a == b else print("false")
# combine conditions
if a > 10 or b < 13:
    print("successful")

if a > 10 and b < 13:
    print("successful")
else:
    print("failed")

# nested
if a > 5:
    print("it's above 5")
    if a > 10:
        print("it's above 10")
    else:
        print("it's not above 10")

# pass, to avoid errors when if statement has no content.
if a < b:
    pass


#=================================
#              WHILE
#=================================

textLoop = "this is a text"
i=0
while i < len(textLoop):
    print(textLoop[i])
    i+=1

# break
i = 0
while i < len(textLoop):
    print(textLoop[i])
    if i == 4:
     break
    i+=1

# continue stops the iteration if the condition is true
i = 0
while i < len(textLoop):
    if i >= 7 and i <= 9:   # to skip " a "
        continue
    print(textLoop[i])
    i+=1
else:
    pass

i = 0
while i < len(textLoop):
    i+=1
    if i >= 7 and i <= 9:   # to skip " a "
        continue
    print(textLoop[i])
else:
    print("no more characters to print.")

#=================================
#               FOR
#=================================

colors = ["red", "yellow", "pink"]
for x in colors:
    print(x)

colors = ["red", "yellow", "pink"]
for x in colors:
    print(x)
    if x == "yellow":
        break

colors = ["red", "yellow", "pink"]
for x in colors:
    if x == "yellow":
        continue     # jump yellow
    print(x)

for x in "colors":
    print(x)

for x in range(5):
    print(x)

for x in range(3,8):
    print(x)

for x in range(3,8,2):
    print(x)
    
for x in range(5):
    print(x)
else:
    print("this is the end!")

common = ["cool", "black", "elegant"]
clothes = ["dress", "shirt", "coat"]
for x in common:
    for y in clothes:
        print(x, y)

for x in []:
    print(x)
else:
    pass # to avoid getting errors when a loop is empty


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

#=================================
#             CLASS
#=================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

John = Person("John", 45)
print(f"{John.name} is {John.age} years old.")

class Person:
    def __init__(selfAlternative, name, age):
        selfAlternative.name = name
        selfAlternative.age = age

    def myfunc(something):
        print("my friend is " + something.name)

PersonX = Person("Josh",89)
PersonX.myfunc()

# changes or delete
PersonX.name = "Joshua"
del PersonX.age
del PersonX

# INHERITANCE
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)  # to keep the inheritance
        self.graduation = year
    
    def message(self):
        print("Welcome", self.name, "to the class of", self.graduation)

Stephen = student("Stephen" , 35, 2025)
Stephen.message()
