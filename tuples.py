
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
