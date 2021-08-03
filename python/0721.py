'''
def get_middle_char(a):
    length = len(a)
    if length % 2 == 1:
        return a[length//2]
    else:
        return a[length//2-1:length//2+1]


print(get_middle_char('ssafy'))
print(get_middle_char('coding'))
'''

'''
def my_func(a,b):
    c=a+b
    print(c)
result = my_func(3,7)
print(result)
'''

'''
def my_avg(*args):
    myList = list(args)
    return sum(myList)/len(myList)
'''

'''
def list_sum(myList):
    sum = 0
    for i in myList:
        sum += i
    return sum

print(list_sum([1,2,3,4,5]))
'''

'''
def dict_list_sum(myList):
    ageSum = 0
    for i in myList:
        ageSum += i['age']
    return ageSum

print(dict_list_sum( [{'name' : 'kim', 'age' : 12},
                      {'name' : 'kim', 'age' : 4}]))
'''


def all_list_sum(myList):
    listSum = 0
    for i in myList:
        for j in i:
            listSum += j
    return(listSum)


print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))
