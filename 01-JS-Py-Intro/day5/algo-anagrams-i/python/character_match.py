# Don't forget to run the tests (and create some of your own)

def quicksort_string(string):
    string1 = list(string)
    if len(string1) <= 1:
        return ''.join(string1)
    else:
        pivot = string1.pop()
        lower_than = []
        greater_than = []
        for character in string1:
            if character > pivot:
                greater_than.append(character)
            else:
                lower_than.append(character)
    return quicksort_string(''.join(lower_than)) + pivot + quicksort_string(''.join(greater_than))

print(quicksort_string("attack"))
print(quicksort_string("zach"))

# Part 1
def is_character_match(string1, string2):
    string_1 = quicksort_string(string1.lower())
    string_2 = quicksort_string(string2.lower())
    return string_1.strip() == string_2.strip()

print(is_character_match('charm', 'march')) #== True)
print(is_character_match('zach', 'attack')) #== False)
print(is_character_match('CharM', 'mARcH')) #== True)
print(is_character_match('abcde2', 'c2abed')) #== True)
print(is_character_match('Anna Madrigal', 'A man and a girl')) # == True

# Part 2
def anagrams_for(word, list_of_words):
    answer = []
    sort_word = quicksort_string(word)
    for word in list_of_words:
        sorted_words = quicksort_string(word)
        if sort_word == sorted_words:
            answer.append(word)
    return answer
print(anagrams_for("threads", ["threads", "trashed", "hardest", "hatreds", "hounds"]))
print(anagrams_for("apple", ["threads", "trashed", "hardest", "hatreds", "hounds"])) #== [])