def fibonacci(n):
  #base case - when to stop
    if n <= 1:
      return n
    else:
      return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(20))


  #      F(n)=f(n-1)+f(n-2)
  #        n = (n-1) + (n-2)
  #        1 = (1-1) + (1-2)
  #        2 = (2-1) + (2-2)
  #        2 = (3-1) + (3-2)
  #        f0 = 0
  #        f1 = 1  
  #        f2 = 0  +  1 = 1
  #        f3 = 1  +  1 = 2
  #        f4 = 2  +  1 = 3
  #        f5 = 3  +  2 = 5
  #        f6 = 5  +  3 = 8
  #
  # print(n)
# fibonacci(5)

# One of the most popular coding challenges is to write an algorithm to return the n-th element in the Fibonacci sequence. 
# Officially, the Fibonacci sequence is the integer sequence defined by the recurrence relation: 
# F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1. For those of us who aren't math whizzes, 
# the nth Fibonacci number is the sum of the prior two Fibonacci numbers.

# Below are the first few values of the sequence:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
# Your challenge today is to write an algorithm that, 

# given a number n, 
#   return the n-th Fibonacci Number. (Keep in mind that the first two numbers in the fibonacci sequence are always [0,1])
    # the nth Fibonacci number is the sum of the prior two Fibonacci numbers.
# Examples:

# find_fibonacci(3) -> 2
# find_fibonacci(7) -> 13