'''
ADMIN FEATURES:
1.Adding_buses
2.Update_booking 
'''
from db import connect
def admin():
    conn=connect()
    cursor=conn.cursor()
    print("""\nAdmin Menu:
       1.Adding buses
       2.Update Bus Details""")
    while True:
        ch=int(input("Enter your choice: "))
        if ch==1:
           adding_buses()
        elif ch==2:
           update_booking()
        else:
           print("Exit")
           break
def adding_buses():
    bus_no=input("Enter bus no: ")
    bus_type=input("Enter bus type: ")
    total_seats=int(input("Enter no. of seats: "))
    Starting_point=input("Enter Starting_point of bus: ")
    Ending_point=input("Enter Ending_point of bus: ")
    Start_time=input("Enter Start_time of bus: ")
    End_time=input("Enter End_time of bus: ")
    Journey_data=input("Enter the date: ")
    fare=int(input("Enter ticket amount: "))
    available_seats=int(input("Enter available_seats: "))
    conn=connect()
    cursor=conn.cursor()
    query="insert into buses values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #%s-this is a phase holder where it holds the values
    values=(bus_no,bus_type,total_seats,Starting_point,Ending_point,Start_time,End_time,Journey_data,fare,available_seats)
    cursor.execute(query,values)
    conn.commit()
    print("Data inserted successfully") 
def update_booking():
   bus_no=input("Enter bus no: ")
   while True:
    print("""\nUpdate Menu:
          1.Starting_point
          2.Ending_point
          3.Start_time
          4.End_time
          5.fare
          6.Exit""")
    ch=int(input("Enter your choice: "))
    if ch==1:
        Starting_point=input("Enter Starting_point of bus to update: ")
        conn=connect()
        cursor=conn.cursor()
        query="update buses set Starting_point=%s where bus_no=%s" #%s-this is a phase holder where it holds the values
        values=(Starting_point,bus_no)
        cursor.execute(query,values)
        conn.commit()
        print("Data updated successfully") 
    elif ch==2:
        Ending_point=input("Enter Ending_point of bus to update: ")
        conn=connect()
        cursor=conn.cursor()
        query="update buses set Ending_point=%s where bus_no=%s" #%s-this is a phase holder where it holds the values
        values=(Ending_point,bus_no)
        cursor.execute(query,values)
        conn.commit()
        print("Data updated successfully") 
    elif ch==3:
        Start_time=input("Enter Start_time of bus to update: ")
        conn=connect()
        cursor=conn.cursor()
        query="update buses set Start_time=%s where bus_no=%s" #%s-this is a phase holder where it holds the values
        values=(Start_time,bus_no)
        cursor.execute(query,values)
        conn.commit()
        print("Data updated successfully")
    elif ch==4:
        End_time=input("Enter End_time of bus to update: ")
        conn=connect()
        cursor=conn.cursor()
        query="update buses set End_time=%s where bus_no=%s" #%s-this is a phase holder where it holds the values
        values=(End_time,bus_no)
        cursor.execute(query,values)
        conn.commit()
        print("Data updated successfully")
    elif ch==5:
        fare=input("Enter ticket amount to update: ")
        conn=connect()
        cursor=conn.cursor()
        query="update buses set fare=%s where bus_no=%s" #%s-this is a phase holder where it holds the values
        values=(fare,bus_no)
        cursor.execute(query,values)
        conn.commit()
        print("Data updated successfully")
    elif ch==6:
        print("Exit")
        break   
if __name__ == "__main__":
      admin()