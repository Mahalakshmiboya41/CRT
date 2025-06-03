'''
x x x 
 x x 
  x
 x x
x x x
'''
rows=3
for i in range(rows,1,-1):
    spaces=' '*(rows-i)
    x='x '*i
    print(spaces+x)
rows=3  
for i in range(1,rows+1):
    spaces=' '*(rows-i)
    x='x '*i
    print(spaces+x)

