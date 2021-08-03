#2021.07.26
#Data structure 
#HOMEWORK
"""
"""
#1
def count_vowels(word):
    # return word.count(['a','e','i','o','u'])
    sum = 0
    vowels = 'aeiou'
    for char in vowels:
        sum+= word.lower().count(char)
    return sum

print(count_vowels('apple'))
print(count_vowels('banana'))
""" 
#2

word = 'select'
print(word.find('s'))
print(word.split('l'))
"""
""" 
#3
def only_square_area(li1,li2):
    ans = []
    for i in li1:
        if i in li2:
            ans.append(i**2)
    return ans
print(only_square_area([32,55,64],[13,32,40,55]))
"""

#workshop
""" 
#1
def get_dict_avg(dict1):
    keys = list(dict1.keys())
    sum = 0
    sub = len(keys)
    for key in keys:
        sum += dict1[key]
    return sum / sub

print(get_dict_avg({
    'python' : 80,
    'algorithm' : 90,
    'django' : 89,
    'web' : 83
    }))
"""
""" 
#2 
def count_blood(bloodList):
    return {key : bloodList.count(key) for key in bloodList }
    
test_blood = [
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB',
]
print(count_blood(test_blood))
"""







