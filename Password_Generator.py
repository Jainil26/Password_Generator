import random

chars = "#$%^&*()_+-=qwertyuiop[]|asdfghjkl;'zxcvbnm,./`"
length = int(input("Enter the length : "))
password = ""
for i in range(length):
    password+=random.choice(chars)

print(password)