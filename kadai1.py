n = 20
for i in range(2,n):
    for j in range(2,i+1):
        if i%j==0 and i!=j:
            print(i)
            break
        elif j==i:
            print(i+1000)
