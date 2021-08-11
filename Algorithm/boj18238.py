
string = input()

prev = 'A'
seconds = 0
for i in range(len(string)):
    check = abs(ord(prev) - ord(string[i]))
    if check <13 :
        seconds += check
    elif check >= 13:
        seconds += 26-check 
    prev = string[i]
print(seconds)
        