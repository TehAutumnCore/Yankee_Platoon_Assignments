def factorial(num):
	# your code here
	pass



# Factorial Challenge
# In this exercise you are going to create a function that takes a number parameter and returns the factorial of it.

# Factorial has a very specific definition. Learn more here. As an overview though, a factorial is the result of multiplying a sequence of descending numbers down to 0. Factorials are only defined for non-negative integer numbers. This definition includes zero. Though 0! is equal to 1, so treat it as an edge case.

# Example
# factorial(4) # => 24 (4 * 3 * 2 * 1)

def factorial(num):
    
    if num <= 1:
        return num
    else:
        return num * factorial(num - 1)
print(factorial(5))

#Take num multiply it by num -1
# !5 = 120
# 5*4*3*2*1