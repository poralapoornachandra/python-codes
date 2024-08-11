#fibonacci series
def fibonacci(num):
    list1 =[0,1]
    a=0
    b=1
    for i in range(2,num):
        c=a+b 
        list1.append(c)
        a=b
        b=c
    print(list1)
n = int(input())
fibonacci(n)