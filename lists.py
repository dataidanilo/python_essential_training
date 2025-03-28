
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
