
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

