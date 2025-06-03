'''
a b c 
 b c 
  c
'''
letters=['a', 'b', 'c']
length=len(letters)

for i in range(length):
    # Print leading spaces
    print(" " * i,end="") 
    # Print letters from i to end separated by space
    for j in range(i,length):
        print(letters[j],end=" ")
    print()
