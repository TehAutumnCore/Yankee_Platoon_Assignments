#Worse case performance is n steps
#where n is length of list
#we use the term Big-O to talk about worst case performance
#O(n) means the worst case performance of an algorithm
#O(n) -> linear performance, increases linearly
#is n steps
# def simple_search(list, target):
    # step = 0
    # for i, element in enumerate(list):
        # print(f"STEP: {step}")
        # if element == target:
            # return i
        # step += 1
        
    #no match return 01
    # return -1
# my_list = list(range(10))

# O(n)
# 2* 10 = 20
# 2* 10 = 20
# 2* 10 = 20
# 2* 10 = 20
# 2* 10 = 20
# print(simple_search(my_list,5000000))

# my_list = {'a','n','b','q','k','i','h','d'}
# print(my_list)
# print(simple_search(my_list,'q'))
# print(simple_search(my_list,'z'))


# n = 8

# step = 0
#n^2 (nested for loop)
#O(n^2)
# for i in range(n):
#     for i in range(n):
#         print(f'STEP: {step}')
#         step +=1

# keep_running = True
# n = 8
# step = 0
# while(keep_running):
#     user_input = input('Type 1 to keep going, 2 to quit: ')
#     step = 0
#     for i in range(10):
#         print(f'STEP {step}')
#         print('something important')
#         step += 1
    
#     if user_input == '2':
#         keep_running = False

#Takes just 1 step to get a thing in a dict
# If we have the key
# This is constant time
#O(1)
# my_dict = {}
# my_dict['a'] = 'a'
# my_dict['b'] = 'b'
# my_dict['c'] = 'c'
# my_dict['d'] = 'd'

# print(my_dict['c'])

def binary_search(lst,target):
    steps = 1 #counter
    low = 0 #list of length 4, list[0] is far left (low)
    high = len(lst)-1 #list of length 4, list[3] is far right (high)
    
    while low <= high:
        mid = (low + high) //2 #round down if len(list is even)
        print(f'STEP: {steps} | Low Index: {low} | Mid Index: {mid} | High Index: {high}')
        print(f"Comparing mid value {lst[mid]} to target {target}")
        # print(mid)
        if lst[mid] == target:
            print("Match!")
            return mid, steps #return tuple of target index, steps
        #go higher
        elif lst[mid] < target:
            print("Mid less than target")
            low = mid + 1
        #go lower
        else:
            print("Mid greater than mid")
            high = mid - 1
        steps += 1
    #not found
    return -1, steps

my_list = list(range(16))
# my_list = list(range(8))
target_index, num_steps = binary_search(my_list,11)
print(my_list[target_index])
    