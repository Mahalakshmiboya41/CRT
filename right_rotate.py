#User function Template for python3


    #Function to rotate an array by d elements in counter-clockwise direction. 
def rotateArr(arr, d):
        #Your code here
        n=len(arr)
        temp=[0]*n
        d=d%n
        for i in range(len(arr)):
            temp[(i+d)%n]=arr[i]
        for i in range(len(arr)):
            arr[i]=temp[i]
        return arr
d=2
arr=[1,2,3,4,5]
print(rotateArr(arr, d))