def linear_search(target, array):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return None

# def linear_search_global(array,target):
#     answer_list = []
#     for i in range(len(array)):
#         if array[i] == target:
#             print(i)
#             answer_list.append(i)
#     return answer_list
# array = ["b", "a", "n", "a", "n", "a", "s"]
# print(linear_search_global(array,"n"))


def linear_search_global(target,arr):
    answer_list = []
    for i, item in enumerate(arr):
        print(f"Index: {i} | Item: {item}")
        if item == target:
            answer_list.append(i)
    return answer_list

array = ["b", "a", "n", "a", "n", "a", "s"]
print(linear_search_global(array,"n"))


#Write a function `linear_search` that takes two arguments: the object 
# (i.e., string or number) you are searching for, and the array you're searching in.  
#Search 
# bananas_list = list('bananas')
# => ["b", "a", "n", "a", "n", "a", "s"]
#value to find, array to search through
#            3,     [1,2,3])        == 2 <-index otherwise return None


#Write a new function `global_linear_search` that returns an array of *all the indices* 
# for the object it searches for.  
# In other words, if the object `x` is in more than one place in the array, 
# `global_linear_search` 
# will return an array containing the index of each occurrence of `x`.

# global_linear_search("a", bananas_list)
# => [ 1, 3, 5 ]

#return indexes of all occurences:
#assert linear_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]) == [1, 3, 5]