import hashlib
import itertools
x = input("Enter the value: ")
found = False
length = 0
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !£$%^&*()_+-={}[]:;@'~#<,>.?/|"
while found != True:
    length = length + 1
    Actual = ""
    for value in itertools.product(string, repeat=length):
        for c in list(value):
            Actual = Actual + c
        hashed = hashlib.md5(Actual.encode()).hexdigest()
        if hashed == x:
            print(Actual)
            found = True
            break
        else:
            Actual = ""
