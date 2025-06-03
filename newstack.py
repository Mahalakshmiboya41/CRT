stack = []
top = -1

def Push(value):
    global top
    stack.append(value)
    top += 1

def pop():
    global top
    if top != -1:
        stack.pop()
        top -= 1
    else:
        print("Stack is empty")

def peek():
    if top == -1:
        return "Stack is empty"
    else:
        return f"Top element = {stack[top]}"

def display():
    if top == -1:
        print("Stack is empty")
    else:
        print("Stack elements (top to bottom):")
        for i in range(top, -1, -1):
            print(stack[i])

while True:
    try:
        user = int(input("Enter a choice(1/2/3/4/5/6): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user == 1:
        value = int(input("Enter value to push: "))
        Push(value)
        print("Pushed:", value)
        print("Current stack:", stack)
    elif user == 2:
        pop()
    elif user == 3:
        result = peek()
        print(result)
    elif user == 4:
        print("Stack:", stack)
    elif user == 5:
        display()
    elif user == 6:
        print("Exiting...")
        break
    else:
        print("Invalid input. Choose between 1-6.")
