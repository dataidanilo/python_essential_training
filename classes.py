
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
