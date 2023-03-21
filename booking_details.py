from tkinter import*
from tkinter import messagebox

root= Tk()
h,w,= root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus_logo =PhotoImage(file=".\\images\\Bus_for_project.png")
Label(root,image = bus_logo).grid(row = 0 ,padx=500, column = 6, columnspan=5)

Label(root,text = "Online Bus Booking System", font = "arial 18 bold",bg = 'sky blue', fg ='Red').grid(row = 1, column = 6, pady = 20,columnspan=6)

def seat_booking():
    root.destroy()
    import s

def check_booked_seat():
    root.destroy()
    import  check_booked_seats

def add_new_details_to_database():
    root.destroy()
    import add_bus_details

Button(root,text="Seat Booking",command=seat_booking,bg = 'green').grid(row=3,column=6,pady=20)
Button(root,text="Check Booked Seat",command=check_booked_seat,bg = 'green').grid(row=3,column=8)
Button(root,text="Add Bus Details",command=add_new_details_to_database,bg = 'green').grid(row=3,column=10)

Label(root,text="For Admin Only",fg="Red").grid(row=4,column=10)


root.mainloop()

