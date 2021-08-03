#Workshop

"""
# 1 
def get_secret_word(myList):
    word = ''
    for cha in myList:
        word += chr(cha)
    return word
print(get_secret_word([83, 115, 65, 102, 89]))
"""

"""
#2
def get_secret_number(word):
    number = 0
    for char in word:
        number += ord(char)
    return number

print(get_secret_number('tom'))
"""

""""""
#3
def get_strong_number(word1, word2):
    def get_secret_number(word):
        number = 0
        for char in word:
            number += ord(char)
        return number
    return word1 if get_secret_number(word1) > get_secret_number(word2) else word2

print(get_strong_number('z', 'a'))
print(get_strong_number('tom', 'john'))