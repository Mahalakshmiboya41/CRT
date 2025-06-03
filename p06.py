'''
1       2       3       4
5                       8
9                       12
13      14      15      16
'''
for i in range(1,5):
    for j in range(1,5):
        if (i==1 or i==4 or j==1 or j==4):
            print(j+(i-1)*4,end="\t")
        else:
            print(" ",end="\t")
    print()
    print()