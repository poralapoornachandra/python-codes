def sum_of_odd_even(num):
    sum1=0
    sum2=0
    list2=[]
    for i in list1:
        if i%2==0:
            sum1 += i
        else:
            sum2 += i
            
    list2.append(sum1) 
    list2.append(sum2)
    print(tuple(list2))
list1 =[1,2,3,4,5,6]
sum_of_odd_even(list1)
