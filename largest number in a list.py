list1 =[4, 7, 1, 8, 3]
list1_max =list1[0]
for i in range(1,len(list1)):
    if list1_max < list1[i]:
        list1_max = list1[i]
print("The largest number in a list is:",list1_max)
