from staff import Staff
from students import Student
class School:
    
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()

    def list_students(self):
        for idx, stud in enumerate(self.students):
            print(f"{idx + 1}. {stud.name} {stud.school_id}")

    def get_student_by_id(self, stud_id):
        for stud in self.students:
            if stud.school_id == stud_id:
                return stud
        return None


    def run_school(self):
        menu = f"""
What would you like to do?
Options:
    1. List All Students
    2. View Individual Student <student_id>
    3. Add a Student
    4. Remove a Student <student_id>
    5. Quit
"""
        while True:
            user_select = input(menu)
            if user_select == '1':
                self.list_students()
            elif user_select == '2':
                stud_id = input("Please enter student id:\n")
                curr_stud = self.get_student_by_id(stud_id)
                if curr_stud:
                    print(curr_stud)
                else:
                    print("There are no students matching these credentials")
            elif user_select == '3':
                print("add a student")
            elif user_select == '4':
                print("remove a student")
            elif user_select == '5':
                print("Come back soon")
                break
            else:
                print("Improper input!")