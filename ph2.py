'''
x x x 
 x x 
  x
'''
rows=3  
for i in range(rows,0,-1):
    spaces=' '*(rows-i)
    x='x '*i
    print(spaces+x)
