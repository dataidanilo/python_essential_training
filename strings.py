
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

