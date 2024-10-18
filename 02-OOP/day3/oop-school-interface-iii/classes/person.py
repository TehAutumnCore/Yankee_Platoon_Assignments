class Person:

    def __init__(self, name, age, password, role):
        self.name = name
        self.age = age
        self.password = password
        self.role = role

    @classmethod
    def all_staff(cls, file_name):
        with open(f"./data/{file_name}.csv") as f:
            reader = csv.DictReader(f)
            list_of_ppl = [cls(**x) for x in reader]
            return list_of_ppl