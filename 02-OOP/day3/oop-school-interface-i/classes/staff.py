import csv

class Staff:
  
  def __init__(self, name,age,role,employee_id,password):
    self.name = name
    self.age = age
    self.role = role
    self.employee_id = employee_id
    self.password = password
  
  def __repr__(self):
    return f"NAME: {self.name} AGE: {self.age}"

  @classmethod
  def all_staff(cls):
    with open("../data/staff.csv") as f:
      reader = csv.DictReader(f)
      staff = [cls(**x) for x in reader]
      return staff
    
print(Staff.all_staff())

# culpepper = Staff("culpepper","25","Principal","86545","xx")
# print(culpepper.name)