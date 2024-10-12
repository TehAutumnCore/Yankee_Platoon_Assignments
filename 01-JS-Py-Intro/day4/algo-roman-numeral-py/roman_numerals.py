roman_numerals = {
    "M" : 1000,
    "D" : 500,
    "C" : 100,
    "L" : 50,
    "X" : 10,
    "V" : 5,
    "I" : 1
}
"""
answer = []
answer.append(num - roman_numerals["M"])
answer.append(num - roman_numerals["M"])
answer.append(num - roman_numerals["M"])
answer.append(num - roman_numerals["M"])
answer.append(num - roman_numerals["M"])
answer.append(num - roman_numerals["M"])
answer.append(num - roman_numerals["M"])
answer.append(num - roman_numerals["M"])
answer.append(num - roman_numerals["M"])
answer.append(num - roman_numerals["M"])
answer.append(num - roman_numerals["M"])
answer.append(num - roman_numerals["M"])
           cant num - 1000 since 345 > roman_numerals["M"]) 
           cant num - 500 since 345 > roman_numerals["D"]) 
answer.append(num - roman_numerals["C"])
answer.append(num - roman_numerals["C"])
answer.append(num - roman_numerals["C"])
answer.append(num - roman_numerals["C"])
           cant num - 50 since 45 > roman_numeral["L"]
answer.append(num - roman_numerals["X"])
answer.append(num - roman_numerals["X"])
answer.append(num - roman_numerals["X"])
answer.append(num - roman_numerals["X"])
answer.append(num - roman_numerals["X"])
           cant num - 10 since 5 > roman_numerals["X"]
answer.append(num - roman_numerals["V"])
"""



def to_roman(num):
    roman_numerals[numeral]


    



"""
def to_roman(num):
    answer=[]
    if num == 0:
        return num
    else:
        pass
    for numeral in roman_numerals:
        if num - numeral != 0:
            num = num - numeral
            answer.append(num)
    return answer.join(" ")
"""


#output expectation
# IV -> 4
# IX -> 9
# XIV -> 14
# XLIV -> 44
# CMXLIV -> 944

#example cases
# print(to_roman(4)) # 'IV'
# to_roman(944) # 'CMXLIV'
# to_roman(150) # CL