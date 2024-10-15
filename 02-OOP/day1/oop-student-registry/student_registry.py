class Student:
    def __init__(self,name,age,grade):
        self._name = name
        self._age = age
        self._grade = grade
    
    def __str__(self):
        return f"Student: Name: {self._name}, Age: {self._age}, Grade: {self._grade}"
    
    @property
    def get_name(self): #Returns students name | N/A|
        return self.name
    
    @property
    #Updates the students name only if the student name <br/> is 3 characters or more, holds no spaces or special characters,<br/> and is in title format | N/A |
    def set_name(self): 
        pass
        
    def get_age(self): #Returns students age | N/A |
        return self.age
    
    #Updates the students age only if the age value is an int <br/>type, is greater than 11, and is lower than 18 | N/A |
    def set_age(self): 
        pass
    
    def get_grade(self): #Returns students grade | N/A |
        return self.grade
    
    #Updates a students grade only if the grade falls within <br/> 9th - 12th grade and the value is formatted with "th" <br/>next to the numbered grade | N/A |
    def set_grade(self): 
        pass
    
    def advance(self,years_advanced):
        new_grade = self.grade + years_advanced
        f"{self.name} has advanced to the {new_grade}th grade"
        
    def study(self,subject):
        f"{self.name} is studying {subject}"