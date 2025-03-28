
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

