# your improved User class goes here

class User:
    posts = []
    #wheels = 4   -> Car.wheels = 5 (this will affect all objects with wheels)
    #if you define a variable above init, it becomes a class variable 
    # To address the variable you must use -> Object.variable
    #variables with values that wont change
    #class namespace
    def __init__(self,name,email,drivers_license = None):
        self.name = name.lower()    #static variables because they can change from object to object
        self.email = email  #instance namespace
        self.drivers_license = drivers_license

    def __str__(self):
        print(f"Name: {self.name} Email: {self.email} Drivers License: {drivers_license}")

    def create_post(self):
        # while len(self.posts) < 5:
        # Create a variable that holds the title of the post
        # Create a variable that holds body of the post
        # build that list and add that list to the list of all posts
        is_valid_title = False
        while is_valid_title is False:
            post_title = input("What would you like the title of the post to be? ").lower()
            if self.name in post_title:
                print(f"{self.name} is in post title")
                is_valid_title = True
            else: #wont make post
                print(f"Your name must be included within the title")
                
        post_body = input("What would you like the body of the post to be? ")
        User.posts.append([post_title,post_body])
    
    def view_post(self):
        for post in User.posts:
            print(post)

    def remove_post_from_all_posts(self,post):
        if post in User.posts:
            User.posts.remove(post)
    
# print(User.__dict__)
gary = User("Gary","Gary@gmail.com","licenseinfohere")
demi = User("Demi","Demi@gmail.com","licenseinfohere")
# gary.bar
gary.myattribute = "hello"
# print(gary.myattribute)
# print(gary.__dict__)
# Jacob = User("Jacob","Jacob@gmail.com","licenseinfohere")
# Juan = User("Juan","Juan@gmail.com","licenseinfohere")

gary.create_post()
# gary.create_post()
gary.view_post()
# print("removing")
# gary.remove_post_from_all_posts("Hello")
# gary.view_post()
# Gary.get_name()
# Demi.get_email()
# Jacob.get_drivers_license()
# Juan.get_name()
