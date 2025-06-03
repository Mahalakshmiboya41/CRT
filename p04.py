'''
* * * * 
* $ $ * 
* $ $ *
* * * *
'''
for i in range(4):
    for j in range(4):
        if 1<=i<=2 and 1<=j<= 2:
            print('$',end=" ")
        else:
            print("*",end=" ")
    print()