'''
1       
1 2     
1 2 3
1 2 3 4
'''
for i in range(4):#(1,5)
    for j in range(4):#(1,5)
        if (i<j):
            print(" ",end=" ")
        else:
            print(j+1,end=" ")#Then print(j)
    print()
    