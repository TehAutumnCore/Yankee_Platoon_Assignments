from dog import Dog

class Cat(Dog):
    species = "Felis catus"
    is_going_to_heaven = False
    
    def __init__(self,name,breed,color):
        super().__init__(name,breed,color)
        print(f"Creating {name}. {name} is of species {Cat.species}")

    def __str__(self):
        return f"Cat name: {self.name}, Cat Species: {self.species}, Cat has {Cat.legs} legs."
    
    def meow(self):
        print(f"{self.name} just meowed!")
        
    def bite(self):
        self.meow()
        print(f"{self.name} bit!")
    
mittens = Cat("Mittens","Moggies","Black and White")
print(mittens)
mittens.bite()
# mittens.bark()
print(Cat)
print(type(Cat))
print(Cat.legs)
print(Cat.is_going_to_heaven)
print(Cat.species)
