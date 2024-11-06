data = [4,3,2,1]

def bubble_sort(lst:list) -> list:
    lngth = len(lst)
    for idx in range(lngth):
        right_limit = lngth - idx - 1
        for jdx in range(0,right_limit):
            print(idx,jdx,right_limit)
            if lst[jdx] > lst[jdx+1]:
                # temporary = lst[jdx+1]
                # lst[jdx+1] = lst[jdx]
                # lst[jdx] = temporary
                lst[jdx], lst[jdx+1] = lst[jdx+1], lst[jdx]
                print(f"""
Current List: {lst}
left cell: {lst[jdx]}
right cell: {lst[jdx+1]}
""")

bubble_sort(data)