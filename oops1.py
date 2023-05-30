class Animal():
    def __init__(self):
        print("Animal created")
    def who_am(self):
        print(" I am animal")
    def eat(self):
        print(" I am eating")

#myanimal = Animal()
# inheritance
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def who_am(self):
        print(" I am dog")
mydog = Dog()
mydog.who_am()
#polymorphism
class rohit():
    def __init__(self,name):
        self.name=name
    def profession(self):
        return self.name + " " + "software tester"

class shruti():
    def __init__(self,name):
        self.name = name
    def profession(self):
        return self.name + " " +"software developer"

myname1 = rohit("Rohit bathla")
myname2 = shruti("Shruti nagpal")
for i in [myname1,myname2]:
    print(i.profession())




