sum=0
n=3645
while(n>0):
    digit=n%10
    sum=digit*digit+sum
    n=n//10
print(sum)