from db import connect
def booking():
    conn=connect()
    cursor=conn.cursor()
def user_details():
    Name=input("Enter name: ")
    Email=input("Enter email: ")
    Phone_no=int(input("Enter phone no.: "))
    conn=connect()
    cursor=conn.cursor()
    query=""
    values=(Name,Email,Phone_no)
    cursor.execute(query,values)
    