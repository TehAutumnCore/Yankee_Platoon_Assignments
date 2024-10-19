class Student:
    """
    Student instance:
    -name
    -id
    -email

    Student class attributes:
        -a list of all the students
        -ids that auto incremement, 0,1,2, etc, so that i need to keep track
        of what the next id should be
    """
    id_counter = 1
    all_students = []
    
    def __init__(self):
        #TODO: Make getters/setters for email, id
        self.name = name
        self.email = email
        print('in __init__ made name and email')
        self.id = Student.id_counter
        
    def __repr__(self):
        return f'Name: {self.name}'
        
        Student.id_counter += 1
        Student.all_students.append(self)