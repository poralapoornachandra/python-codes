n=input()
def reverse_string(num1):
    str1 = ""
    for i in range(len(n)):
        str1 = n[i] + str1
    print(str1)
reverse_string(n)
