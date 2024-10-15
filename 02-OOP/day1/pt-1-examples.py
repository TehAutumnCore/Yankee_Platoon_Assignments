#Create a class

class Dog:
    #Double underscores (dunder) indicate programmers should NOT class this method directly; The python runtime will do it for us at the right time
    #sometimes called the constructor, class constructor, constructor method
    def __init__(self,name,breed, color, sound):
        print(f"This dog is named {name}, {name} is a {color} {breed}. When {name} talks they say {sound}")
        
        #creating a class instance attributes
        self.name = name
        self.breed = breed
        self.color = color
        self.sound = sound
        self.fetch_items = []
        self.foo = None
    
    def __str__(self):
        return f"Name: {self.name}, Breed: {self.breed}, Color: {self.color}, Sound: {self.sound}"
    
    def speak(self):
        print(f'{self.name} says: {self.sound}')
    
    def fetch(self,item):
        print(f'{self.name} fetched the {item}')
        self.fetch_items = [item]
        self.fetch_items.append(item)
        
#Constructing an instance of a class, aka instantiating a class instance, creating a Dog object, etc.
#This calls the class's __init__() method, or , python just creates the instance if __init__ doesnt exist
fido = Dog('fido','Pointer','white','woof!')
rover = Dog('Rover','Golden Retreiver','golden','bark!')

print(fido)

# print('Fido')
# print(fido.name)
# print(fido.color)
# print()
# fido.fetch('ball')
# print('')

# print('Rover:')
# rover.speak()
# rover.fetch('stick')
print('Rover: ')
print(rover)
# my_list = []
# print(rover.fetch_items)
# print(rover.name)
# print(rover.color)
# print(rover.color)
# print('')