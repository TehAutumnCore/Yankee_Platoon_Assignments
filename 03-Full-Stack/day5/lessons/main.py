#Log of n is a number multiplied by itself by 2
log_of_2_by_16 = 4 #16
# print(2*2*2*2)

log_of_2_by_128 = 7 #128
# print(2*2*2*2*2*2*2)

#linear time - o(n)
def simple_search(lst:list[int], tgt:int)->int: #typecasting to help self code. ->return int
    for x in range(len(lst)):
        if lst[x] == tgt:
            return x #measuring by worse case scenario
    return -1

# print(simple_search(list(range(1,1000)),999))


# ologn
def binary_search(lst:list[int],tgt:int) -> int:
    left = 0
    right = len(lst)-1
    while left <= right:
        mid = (right + left)// 2
        if lst[mid] == tgt:
            return mid
        elif lst[mid] > tgt:
            right = mid -1
        else:
            left = mid + 1
    return -1
# print(binary_search(list(range(1,101)),100))


#const time will always be O(1) regardless of input since it has direct access. Dictionaries also have const time
def access_element(lst:list[str],idx:int): 
    return lst[idx]
# print(access_element()

#O(log^2) quadratic
def bubble_sort(lst:list[int],list[int]):
    n = len(lst)
    for idx in range(n):
        for jdx in range(0,n-idx - 1):
            print(lst)
            if lst[jdx] > lst[jdx + 1]:
                lst[jdx], lst[jdx + 1] = lst[jdx + 1], lst[jdx]
    return lst
# print(bubble_sort([2,1,3,5,6,4]))

