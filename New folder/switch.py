def vowels(n):
    count = 0
    for i in n:
        if i in "aeiouAEIOU":
            count += 1
    return count
def odd_even(n):
    odd = 0
    even = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even
def duplicate(n):
    remove = list(set(n))
    return remove
def diamond(n):
    for i in range(n):
        for j in range(0, n - i - 1):
            print(end=" ")
        for j in range(0, i + 1):
            print("*", end=" ")
        print()
    for i in range(n):
        for j in range(0, i + 1):
            print(end=" ")
        for j in range(0, n - i - 1):
            print("*", end=" ")
        print()
ch = input("Enter your choice: \n1. vowels \n2. odd or even \n3. duplicates \n4. diamond\n")
if ch == "1":
    n = input("Enter string: ")
    print("Number of vowels:", vowels(n))
elif ch == "2":
    n = int(input("Enter the number: "))
    odd, even = odd_even(n)
    print("Odd:", odd, "Even:", even)
elif ch == "3":
    n = input("Enter string: ")
    print("Corrected:", duplicate(n))
elif ch == "4":
    n = int(input("Enter rows: "))
    diamond(n)
else:
    print("Invalid choice")
