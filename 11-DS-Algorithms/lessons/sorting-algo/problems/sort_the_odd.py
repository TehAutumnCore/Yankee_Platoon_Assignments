def sort_array(lst:list[int]->list[int])
    
    def is_odd(num:int)->bool:
        return bool(num % 2)
    
    for idx in range(1,len(lst)):
        item = lst[idx]
        jdx = idx -1
        print(f"""
item:{item},
jdx_value{lst[jdx]}
item_is_odd:{is_odd(item)}
""")
        while jdx >= 0 and item< lst[jdx] and is_odd(item):
            lst[jdx+1] = lst[jdx]
            jdx -= 1
            print(lst)
        lst[jdx+1] = item
        print(f"\n{lst}\n")
    return lst
        
        
        
sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])