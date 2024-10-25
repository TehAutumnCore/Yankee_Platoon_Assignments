def solution(n):
    roman_numerals = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}       
    answer_list = []
    print(f"Converting {n} to Roman numerals.")
    
    # for key,value in roman_numerals.items():
    #     while n >= value: #while n != 0       
    #         answer_list.append(key)
    #         n -= value
    #         print(f"Added '{key}', remaining value to convert: {n}")
    
    for key,value in roman_numerals.items():
        if n >= value: 
            temp = n % value #1 = 2001 % 1000
            times = (n - temp) / value
            n = temp
            answer_list.append(key*times)
    result = "".join(answer_list)
    print(f"Final Roman numeral: {result}")
    return result
solution(2001) #'MCMLXXXIX', "solution(1989),'MCMLXXXIX'"



"""
We want to:
use n and subtract the value of the key 'm' if so
    if leftover == 0
        return n
    else:
        #Loop through keys & values of the roman numerals dictionary
        
            if the remaining is > 'm'(1000) #dictionary value
                subtract m and append to list        
            else:
                leftover == 0
    return ",".join(answer_list)
"""
# print(roman_numerals[])
    # for key,value in roman_numerals.items():
    #     total = n
    #     # total -= roman_numerals[value] #1989 -> 989
    #     # print(key)
    # print(value)
