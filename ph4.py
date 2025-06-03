'''
      A 
    A B 
  A B C
A B C D
'''
for i in range(1, 5):
    k=0  # Initialize character index
    for j in range(1, 5):
        if i+j>=5:
            print(chr(65 + k), end=" ")  # chr(65) = 'A'
            k+=1
        else:
            print(" ",end=" ")
    print()
