# Implementing push operation in a stack.
# The size of the stack is not defined in this.
# In this top is useless.
stack=[]
top=-1 # It is a local varialble
size=5 #This should given for static length
def Push(value):
    global top # By doing this it becomes a global varaible
    if(top==size-1):
        return "Stack is full"
    else:
        return stack.append(value)
        top+=1
# To pop the value we have to check whether the stack is empty or not.
def pop():
    global top
    if(top!=-1):
        return stack.pop()
    else:
        return "stack is empty"
        top-=1
def peek():
    if(top==-1):
        return "Stack is empty"
    else:
        return f"Top element = {stack[top]}"
def display():
    if(top==-1):
        return "stack is empty"
    else:
        for i in range (top,-1,-1):
           print(stack[i])
Push(10)
Push(20)
Push(30)
Push(40)
Push(50)
Push(60)
pop()
pop()
pop()
pop()
print(peek())
print(stack)
display()
