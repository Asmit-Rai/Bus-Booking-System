from tkinter import*
import sqlite3
from tkinter import messagebox
root= Tk()
root.state('zoomed')

bus_logo =PhotoImage(file=".\\images\\Bus_for_project.png")
Label(root,image = bus_logo).grid(row = 0 , column = 6,columnspan=15)

Label(root,text = "Online Bus Booking System", font = "Arial 20 ",bg = 'sky blue', fg ='Red').grid(row = 1, column = 6, pady = 20,columnspan=15)

Label(root,text = "Add Bus Route Details", font = "arial 10 ",bg = 'light green', fg ='green').grid(row = 2, column = 6, pady = 15,columnspan=15)

Label(root,text = "Route Id").grid(row=3 , column = 2)
route_id=Entry(root)
route_id.grid(row = 3 , column =3)

Label(root,text = "Station Name").grid(row=3 , column = 4)
station_name=Entry(root)
station_name.grid(row = 3 , column =5)

Label(root,text = "Station Id").grid(row=3 , column = 6)
station_id=Entry(root)
station_id.grid(row = 3 , column =7)





def add_route():
    con=sqlite3.Connection("Bus_database")
    cur=con.cursor()
    
    if route_id.get()!="" and station_name.get()!="" and station_id.get()!="" :
        cur.execute("insert into Route_details values('"+route_id.get()+"','"+station_name.get()+"','"+station_id.get()+"')")
        con.commit()
        display()
        con.close()
        messagebox.showinfo("","Route details added successfully")
    else:
        messagebox.showerror("","Please fill all the field")
Button(root, text= 'Add Route',fg ='black' ,bg= 'light green',command=add_route).grid(row= 3 ,column = 8)



def display():
    Label(root,text=route_id.get()+" "+station_name.get()+" "+station_id.get()).grid(row=4,column=5)





def delete_route():
    con=sqlite3.Connection("Bus_database")
    cur=con.cursor()
    if route_id.get()!="" and station_name.get()!="" and station_id.get()!="" :
        
        cur.execute("DELETE FROM Route_details(R_Id,S_Id,Sname) VALUES (?,?,?)",(route_id.get(),station_name.get(),station_id.get()))
        messagebox.showinfo("","Route details deleted successfully")
    else:
        messagebox.showerror("","Please fill all the field")
Button(root, text= 'Delete Route',fg ='black',bg='Red',command=delete_route).grid(row= 3 ,column = 10)




def home():
    root.destroy()
    import add_bus_details 

home_logo =PhotoImage(file=".\\images\\home.png")
Button(root,fg ='black' ,bg= 'light green',image = home_logo,command=home).grid(row= 4 ,column = 10, padx = 10)


root.mainloop()
