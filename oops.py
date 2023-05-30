
class Dog():
    species = 'mammal'
    def __init__(self ,breed ,name ,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self,number):

        print("bark my name is {} my number {}" .format(self.name,number))

my_dog = Dog('lab','hankins',False)
print(my_dog.breed,my_dog.name,my_dog.spots,my_dog.species)
my_dog.bark(5)