# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
#             "o","p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# import string #imports the string module

# alphabet = string.ascii_lowercase #provides a list of a-z in lowercase

# def caesar_cipher(cipher_string, shift_amount):
#     answer_list = [] #answer list
#     for char in cipher_string: #for every character in cipher_string
#         if char.isalpha(): #checks if the character is an alphabatical letter
#             shifted_index = (alphabet.index(char.lower()) + shift_amount) % 26 #returns the index of character with .lower() + shift amount) % 26 to get the remainder
#             #Preserve case - keeps the original capitalization of text
#             if char.isupper(): #returns true or false if the character is uppercase
#                 answer_list.append(alphabet[shifted_index].upper()) #appends the new letter grabbed from shifted index and uppercases it
#             else:
#                 answer_list.append(alphabet[shifted_index]) #appends the new letter grabbed from the shifted index
#         else:
#             answer_list.append(char) #if the character isn't an alphabetical character append to answer_list
#     print(''.join(answer_list)) #prints the results
#     return ''.join(answer_list) #returns the results
















# def caesar_cipher(string, shift_amount):
# cipher_string = "xyz" #  "Wjt! Rcvo v nomdib!"
# shift_amount = -23 # W wraps over a
# shift_amount = 4 # W wraps over z
# shift_amount = 3 # wraps over z
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
            "o","p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
string = "Boy! What a string!"
shift_amount = -5
answer_list = []
split_string = list(string.lower()) #-> ['W', 'h', 'a', 't', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g', '!'] 
# print(split_string)
for letter in split_string:
    if letter in alphabet:
        shifted = alphabet.index(letter)+shift_amount
        # print(alphabet[shifted])
        if shifted < 0: #if the index is less than 0, start count back from 25
            remainder = (shifted + 26) % len(alphabet) # To compensate for it being negative and so it stays within range of index 0-25
            answer_list.append(alphabet[remainder])
            # print(alphabet[remainder])
        elif shifted > 25: #if the index is more than 25, start counting from 0
            remainder = shifted % len(alphabet) #returning the letter at position[remainder]
            answer_list.append(alphabet[remainder]) # To compensate for it being above the length range and so it stays within range of index 0-25
            # print(alphabet[remainder])
        else:
            answer_list.append(alphabet[shifted]) # The shifted is the new indexOf the original string but it is now shifted by the new index (alpa.) and corresponds to the new indexOf which appends the indexOf (alpha.) to answer_list
    else: #if the letter was not in alphabet
        answer_list.append(letter)   
    # print(shifted) 


result = ''.join(answer_list) #--> wjt! rcvo v nomdib!          result
print(result)


# print(result)   Looking for #-->"Wjt! Rcvo v nomdib!"         answer 
#                                 "Boy! What a string!"         string
#                                 [0]  [5]
# idk how to regex in python  pattern = [!@#$$%^%^&**()] we only need it for special chars


