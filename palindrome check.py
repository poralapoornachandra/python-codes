n=input()
def palindrome(n):
    str1 =""
    for i in range(len(n)):
        str1 = n[i] + str1
    if str1 == n:
        print(f"{n} is a palindrome")
    else:
        print(f"{n} is not a palindrome")
palindrome(n)
