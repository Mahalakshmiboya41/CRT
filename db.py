import mysql.connector
def connect():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sruthip0222@",
        database="Bus_booking_management"
    )
    return conn
if(connect()):
    print("Connection established successfully")
else:
    print("Connection failed")