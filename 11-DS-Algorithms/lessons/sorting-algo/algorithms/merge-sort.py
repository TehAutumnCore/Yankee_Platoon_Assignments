def merge_sort(items):
    #find the length of our list to track our loop
    items_len = len(items)
    #Checking if the list has one or less items, if so return list because it is sorted
    if items_len <= 1:
        return items
    sublist_len = 1
    while sublist_len < items_len:
        for i in range(0, items_len, 2 * sublist_len):
            left_sublist = items[i:1 + sublist_len]
            right_sublist = items[i + sublist_len: i + 2 * sublist_len] #items[1:2]
            #left_sublist = 2
            #right_sublist = 8
            merged_sublist = merge(left_sublist, right_sublist)

            items[i : i +len(merged_sublist)] = merged_sublist
        sublist_len *= 2
            
def merge(left, right):
    result = []
    i, j = 0,0
        #[2] [8]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
        else: #right < left
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i +=1
    while j < len(right):
        result.append(right[j])
        j +=1
sorted = merge_sort
print(sorted)