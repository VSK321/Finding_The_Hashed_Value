import hashlib
import itertools
x = input("Enter the value: ")
found = False
length = 0
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !£$%^&*()_+-={}[]:;@'~#<,>.?/|"
Actual = ""
while found != True:
    length = length + 1
    for value in itertools.product(string, repeat=length):
        for c in list(value):
            Actual = Actual + c
        hashed = hashlib.md5(Actual.encode()).hexdigest() #This is currently an MD5 hash but can be changed to be any other that is included in the hashlib module
        if hashed == x:
            print(Actual)
            found = True
            break
        else:
            Actual = ""
