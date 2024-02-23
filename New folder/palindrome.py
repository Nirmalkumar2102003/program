pal = [323, 121, 54345, 8796978]
def palindrome(n):
    return str(n) == str(n)[::-1]
largest = 0
for n in pal:
    if palindrome(n):
        if n > largest:
         largest = n
print("The largest palindrome number is:", largest)
