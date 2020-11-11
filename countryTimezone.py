from tkinter import * 
import time
from tkinter import ttk
import pytz 
from pytz import timezone
from datetime import datetime


class Clock():
    def __init__(self, master):
        
        self.master = master
        master.geometry("480x360")

        self.frame = Frame(master, borderwidth=5, relief="sunken")
        self.frame.pack(fill=BOTH, expand=True)

        self.select_country = Label(self.frame, text="select country", font="helvetica 14")
        self.select_country.place(x=175, y=50)


        self.select_country_combo = ttk.Combobox(self.frame, width = 30, values=pytz.all_timezones, state="readonly", font="verdana 10")
        self.select_country_combo.place(x=100, y=100)

        self.show_button = Button(self.frame, text="SHOW", width=10, height=1, font="helvetica 8", bd=3, command=self.time)
        self.show_button.place(x=190, y=140)

        self.time_label = Label(self.frame, font="helvetica 32", fg='red')
		
        

    def time(self):

        fmt = "%H:%M:%S"
        self.timezone_var = pytz.timezone(str(self.select_country_combo.get()))
        self.get_timezone = datetime.now(self.timezone_var)
        self.time_last = self.get_timezone.strftime(fmt)
        self.time_label.configure(text=self.time_last)
        self.time_label.place(x=140, y=240)
        tk.after(1000, self.time)


        

tk = Tk()
app=Clock(tk)
tk.mainloop()






