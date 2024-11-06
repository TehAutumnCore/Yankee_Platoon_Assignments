data = [4,3,2,1]
def insertion(lst:list[int]) -> list[int]:
    for idx in range(1, len(lst)):
        item = lst[idx]
        
        jdx = idx - 1
        
        while jdx >=0 and item < lst[jdx]:
            print(f"""
item: {item}
jdx: {jdx}
value: {lst[jdx]}
list: {lst}       
""")
            lst[jdx+1] = lst[jdx]
            jdx -=1
            
        lst[jdx+1] = item
    return lst

print(insertion(data))