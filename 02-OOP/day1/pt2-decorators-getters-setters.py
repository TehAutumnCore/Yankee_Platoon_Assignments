# def my_decorator(func):
#     print('inside my_decorator()')
          
# def wrapper_function():
#     print('inside wrapper_function(), about to call func')
#     func() #call the function passed in as an arg
#     print('func function has been called!!!')
#     print("...the message has been delivered")
    
#     return wrapper_function


# @my_decorator    
# def wrapped_say_hi():
#     print('hello, world')

# @my_decorator
# def wrapped_say_bye():
#     print('goodbye')

# say_hi()

# wrapped_say_hi = my_decorator(say_hi)
# wrapped_say_hi()

# wrapped_bye = my_decorator(say_bye)
# wrapped_bye()

#my_decorator


#say_hi()



"""
Getters and setters are good for ...
-validating data
-formatting data to show users
-applying other logic to data
"""
class Person:
    def __init__(self,name,age):
        self._name = name.lower()
        self._age = age
    
    #SELECT NAME WHERE NAME == 'ALICE'
    
    #getter
    @property
    def name(self):
        return self._name
    
    #setter
    @property
    def name(self):
        return self._name.capitalize()
    
    @name.setter
    def name(self,new_name):
        if isinstance(new_name,str) and len(new_name) >= 3:
            self._name = new_name.lower()
        else:
            print('Name must be a string at least 3 characters long')
    
alice = Person('Alice',20)
print(alice.name)

alice.name = 7
print(alice._name)
print(alice.name)