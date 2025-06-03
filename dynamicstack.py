#dynamic(without any size fixation before it self)
stack=[]
top=-1
def Push(value):
    global top
    stack.append(value)
    top+=1
def pop():
    global top
    if(top!=-1):
        stack.pop()
        top-=1
    else:
        return "stack is empty"
def peek():
    if(top==-1):
        return "Stack is empty"
    else:
        return f"Top element = {stack[top]}" # Here top holds index of top value
def display(): # This is used to print the values in the LIFO order
    if(top==-1):
        return "stack is empty"
    else:
        for i in range (top,-1,-1):
           print(stack[i])
while True:
    user=int(input("Enter a choice(1/2/3/4/5/6):"))
    if(user==1):
        value=int(input("Enter value to push: "))
        Push(value)
        print(stack)
    elif(user==2):
        pop()
    elif(user==3):
        print(peek())
    elif(user==4):
        print(stack)
    elif(user==5):
       display()
    elif(user==6):
        print("exit")
        break
    