from db import connect
def booking():
    Starting_point=input("Enter Starting_point of bus: ")
    Ending_point=input("Enter Ending_point of bus: ")
    conn=connect()
    cursor=conn.cursor()
    query="select*from buses where starting_point=%s and ending_point=%s"
    values=(Starting_point,Ending_point)
    cursor.execute(query,values)
    results=cursor.fetchall()
    if not results:
        print("No buses found for this route.")
        conn.close()
        return
    print("Matching Buses:")
    for row in results:
            bus_no,bus_type,seats,start, end,start_time,end_time,journey_date,fare,available_seats=row
            start_str=str(start_time)
            end_str=str(end_time)
            print(f"{bus_no}|{bus_type}|{start}→{end}|{start_str}|{end_str}|{journey_date}|{seats}|{fare}|{available_seats}")
    user=input("Enter the bus_no: ")
    query="select*from buses where bus_no=%s and starting_point=%s and ending_point=%s"
    values=(user,Starting_point,Ending_point)
    cursor.execute(query,values)
    result=cursor.fetchone()
    if not result:
       print("Invalid bus number selected.")
    else:
        available_seats=result[9]  
        print(f"Available seats for {user}:{available_seats}")
    if available_seats==0:
            print("No seats available.")
    else:
         seats_to_book=int(input("Enter no. of seats for booking: "))
         if seats_to_book>available_seats:
            print("Not enough seats avilable.")
         else:
            new_seat_count=available_seats-seats_to_book
            update_query="update buses set available_seats=%s where bus_no=%s"
            values=(new_seat_count,user)
            cursor.execute(update_query,values)
            conn.commit()
            print(f"{seats_to_book} seat(s) booked successfully for bus {user}.")
    Name=input("Enter name: ")
    Email=input("Enter email: ")
    Phone_no=input("Enter phone no.: ")
    insert_query="""
    INSERT INTO booking_details (bus_no, name, email, phone_no, seats_booked)
    VALUES (%s, %s, %s, %s, %s)
    """
    booking_data =(user,Name,Email,Phone_no,seats_to_book)
    cursor.execute(insert_query,booking_data)
    conn.commit()
    print("Booking details saved successfully.")

    # name=input("Enter name: ")
    # email=input("Enter email: ")
    # phone_no=input("Enter phone no.: ")
    # insert_user="insert into users values(%s, %s, %s)"
    # values=(name,email,phone_no)
    # cursor.execute(insert_user,values)
    # user_id=cursor.lastrowid
    # insert_booking="insert into booking_details values (%s, %s, %s, %s)"
    # values=(user,user_id,seats_to_book,'confirmed')
    # cursor.execute(insert_booking,values)
    # new_seat_count=available_seats-seats_to_book
    # update_seats="UPDATE buses SET available_seats=%s WHERE bus_no=%s"
    # cursor.execute(update_seats, (new_seat_count,user))
    # conn.commit()
    # print(f"{seats_to_book} seat(s) successfully booked for {name} on bus {user}.")
    # conn.close()

if __name__ == "__main__":
       booking()