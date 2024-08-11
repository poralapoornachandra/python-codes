def even_and_odd_num(num):
    list2 =[]
    list3 =[]
    for i in num:
        if i%2==0:
            list2.append(i)
        else:
            list3.append(i)
    print("Even list is:",list2)
    print("Odd list is:",list3)
list1 =[1,2,3,4,5,6]
even_and_odd_num(list1)
