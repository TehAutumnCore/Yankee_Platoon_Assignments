import csv

# drawsql
# https://drawsql.app/teams/franciscos-team-2-1/diagrams/yankee


class Student:
    students = {}

    def __init__(self, id, first_name, last_name, age, grade):
        self._id = int(id)
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self._grade = grade

    @classmethod
    def load_data(cls):
        with open("./students.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["grade"].upper() in ["A", "B", "C", "D", "F"]:
                    row["grade"] = row["grade"].upper()
                else:
                    print("Grade must be of value A, B, C, D, F")
                if row["first_name"].isalpha():
                    row["first_name"] = row["first_name"].title()
                else:
                    print("All characters in a name must be letters")
                if row["last_name"].isalpha():
                    row["last_name"] = row["last_name"].title()
                else:
                    print("All characters in last name must be letters")
                if row["age"].isnumeric() and row["id"].isnumeric():
                    row["id"] = int(row["id"])
                    cls.students[row["id"]] = cls(**row)
                else:
                    print("Age and ID must be of integer value")


Student.load_data()
print(Student.students[6].age)
