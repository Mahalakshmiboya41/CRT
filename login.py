from db import connect
from booking import booking
def auth():
    conn=connect()
    cursor=conn.cursor()
    print("""\nSignup/Login
       1.Sign Up
       2.Login""")
    ch=int(input("Enter your choice: "))
    if ch==1:
       signup()
    elif ch==2:
        login()

def signup():
    print("Sign Up")
    username=input("Create username: ")
    password=input("Create password: ")
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("select * from users where username=%s",(username,))
    if cursor.fetchone():
        print("Username already exists.Please try logging in.")
    else:
        cursor.execute("insert into users values (%s,%s)",(username,password))
        conn.commit()
        print("Account created successfully! You can now log in.")
        login()
def login():
    print("Welcome to Bus Booking Management System")
    username=input("Enter username: ")
    password=input("Enter password: ")
    conn=connect()
    cursor=conn.cursor()
    query="select*from users where username=%s and password=%s"
    values=(username,password)
    cursor.execute(query,values)
    result=cursor.fetchone()
    if result:
        print("Login successful! Welcome,",(username,))
        booking()
    else:
        print("Login failed! Invalid username or password.")
    conn.close()
if __name__ == "__main__":
    auth()
