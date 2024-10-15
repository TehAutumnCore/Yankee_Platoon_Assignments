# your User class goes here

class User:
    
    def __init__(self,name,email,drivers_license = None):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license

    def __str__(self):
        print(f"Name: {self.name} Email: {self.email} Drivers License: {drivers_license}")
    
# Gary = User("Gary","Gary@gmail.com","licenseinfohere")
# Demi = User("Demi","Demi@gmail.com","licenseinfohere")
# Jacob = User("Jacob","Jacob@gmail.com","licenseinfohere")
# Juan = User("Juan","Juan@gmail.com","licenseinfohere")

# Gary.get_name()
# Demi.get_email()
# Jacob.get_drivers_license()
# Juan.get_name()
