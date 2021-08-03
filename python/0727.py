#homework

""" 
#1 
myList = [3,25,62,43,2,5]
print('myList :', myList)
print('returned from sorted() :', sorted(myList))
print('myList after sorted() :', myList)
print('returned from .sort() :', myList.sort())
print('myList after .sort() :', myList)
"""

""" 
#2
myList = [3,25,62,43,2,5]
myList.extend([1,2,3])
print(myList) #[3, 25, 62, 43, 2, 5, 1, 2, 3]
myList.append([1,2])
print(myList) #[3, 25, 62, 43, 2, 5, 1, 2, 3, [1, 2]]
"""

""" 
#3
a = [1,2,3,4,5]
b = a

a[2] = 5

print(id(a))
print(id(b))
"""

#workshop

"""
 #1 
def duplicated_letters(word):
    charSet = set()
    for char in word:
        if word.count(char)>1:
         charSet.add(char)
    return list(charSet)

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))
"""
#comprehension
def duplicated_letters(word):
    return list({char for char in word if word.count(char)>1})

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))

"""
 #2
def low_and_up(word):
    index = 0
    retWord = ''
    for char in word:
        if index%2==0:
            retWord += char.lower()
        else :
            retWord += char.upper()
        index+=1
    return retWord
print(low_and_up('apple'))
print(low_and_up('banana'))
"""

"""
 #3
def lonely(numList):
    prev = 10
    retList = []
    for num in numList:
        if num!=prev:
            retList.append(num)
        prev = num
    return retList

print(lonely([1,1,3,3,0,1,1]))
print(lonely([4,4,4,3,3]))
"""