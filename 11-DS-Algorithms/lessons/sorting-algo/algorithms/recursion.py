# def count_down(n):
#     if n == 0:
#         return
#     else:
#         print(n)
#         countdown(n-1)
# count_down(5)

# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         # print(n)
#         return n * factorial(n-1)
# print(factorial(5))


def factorial(n, current = 1):
    if current > n:
        return 1
    else:
        print(current)
        return current * factorial(n+1)

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(12))