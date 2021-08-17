
#input 
word = input()

#lists
alpha = []
num = []

for char in word:
    if char.isalpha():
        alpha.append(char)
    else:
        num.append(char)

alpha.sort()
num.sort()
alpha.extend(num)
for char in alpha:
    print(char, end='')