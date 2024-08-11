def multiples(num, limit):
    for i in range(num, limit + 1, num):
        print(i,end=",")

multiples(3, 20)
