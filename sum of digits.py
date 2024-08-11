n=int(input())
sum =0
while(n!=0):
    p=n%10
    sum = sum + p 
    n=n//10
print(f"sum is {sum}")
