class Mother:
    def __init__(self):
        print('Mother.__init__()')
        self.first_name = 'Sandra'
        self.last_name = 'Wilensky'

class Father:
    def __init__(self):
        print('Father.__init__()')
        self.first_name = 'Harris'
        self.last_name = 'Cohen'
        
class Child(Mother,Father): #first arguement is what is called first
    def __init__(self, first_name):
        # super().__init__()
        Mother.__init__(self) #if you call bother parents, then order in arguements dont matter
        Father.__init__(self) #if you use multiple inheritance use this
        self.first_name = first_name
        print('Child.__init__()')
        
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    
class Grandchild(Child):
    def __init__(self,first_name):
        super().__init__(first_name)
        self.first_name = first_name