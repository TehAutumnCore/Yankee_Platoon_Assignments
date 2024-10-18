#parent class
class Animal:
    foo = 'hello'
    def __init__(self,name,species,sound = 'Default Animal Sound'):
        print("Animal.__init__() name:{name} species:{species}")
        self.name = name
        self.species = species
        self.sound = sound
        
    def __repr__(self):
        return f"I'm an animal named {self.name}. My species is {self.species}"
    #return f"{self.name} Species: {self.species}"
        
    def eat(self):
        print(f'{self.name} eats')
        
    def make_sound(self):
        print(f"{self.name} says {self.sound}")
# polly = Animal("polly","parakeet")
# print(polly)

















##########################################################################################################################
#children classes


class Dog(Animal):
    def __init__(self,name,breed):
        #returns the parent class
        super().__init__(name,"Dog")
        # parent = super()
        # print(f'parent class attribute foo {parent.foo}') #same as Animal.foo
        # Animal.__init__(name,"dog")
        # Animal(name,"Dog")
        # parent.__init__(name,species="Dog")
        
        # self.name = name
        self.breed = breed
        
    def bark(self):
        return "woof!"   
      
        
daryl = Dog('daryl','golden doodle')
daryl.make_sound()
# print(daryl.__dict__)
# print(dir(daryl))
print(f"printing the dog {daryl}")
daryl.eat()

class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name,"Cat", 'meow!')
        print(f'Making a {self.species} named {self.name} that makes a sound {self.sound}')
        print('Cat.__init__()')
        
        self.color = color
    
    def clean_litterbox(self):
        print(f"{self.name} cleans litterbox")
    
    # def make_sound(self):
        # return f"meow!"
    
garfield = Cat('garfield', 'orange')
# print(garfield)
# print(garfield.__dict__)
# garfield.make_sound()
# print(dir(garfield))
# garfield.eat()
