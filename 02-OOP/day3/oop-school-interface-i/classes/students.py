import csv
class Students:
    
    def __init__(self,name,age,role,school_id,password):
        self.name = name
        self.age = age
        self.role = role
        self.school_id = school_id
        self.password = password

    @classmethod 
    def all_students(cls):
        #open the csv
        # students = []
        with open("../data/students.csv",'r') as student_file:
            ## I want to create dicts from csv lines
            reader = csv.DictReader(student_file) #can iterate through
            students = [csv(**x) for x in reader]
            return students
            ## Iterate through list of dicts  students = [cls(**x) for x in reader]
            # for row in reader:
                #create class instances per dict
                #append instance into list
                # students.append(cls(**row))
                #return list of cls instances
        # print(students)
        # return students
                
Students.all_students()    
                
# diana_dict = {
#     "name":"Diana",
#     "age": 17,
#     "password": "password",
#     "role": "Students",
#     "school_id" : 123345
# }

# diana =Student(name='Diana',age=17,password='password',role='Student',school_id 12345)
# diana = Student(**diana) #matches key to arguement within the init
# print(diana.name)