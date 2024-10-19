class Dog:
    #Class Attributes
    legs = 4
    is_going_to_heaven = True
    species = "Canis Lupus Familiaris"
    
    def __init__(self,name,breed,color):
        self._name = name
        self.breed = breed
        self.color = color
    
        decription = f"Creating {name}. {name} is of species {Dog.species}"
    
    def __str__(self):
        return f"Dog name: {self.name}, Dog Breed: {Dog.species}, has {Dog.legs} legs."

    def __bark(self):
        print(f"{self.name} just barked!")
    
    def bite(self):
        self.bark()
        print(f"{self.name} bit!")
    
    @property
    def name(self):
        return self._name.capitalize()    
    
    @name.setter
    def name(self,new_name):
        if len(new_name) < 3:
            print('Name must be atleast 3 characters long')
        else:
            self._name = new_name