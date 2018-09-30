from tkinter import *
from win10toast import ToastNotifier
from datetime import datetime, timedelta

import os.path

VERSION=1.0

class Create(Frame):
    
    def __init__(self, master):
        self.master = master
        master.title("Post It Notes")

        self.help = "Type your text here"

        self.postitems = []

        #Reminder
        self.reminder_entry = Text(master)
        self.reminder_entry.pack(side=LEFT, fill=BOTH, expand=True,
                                 padx=5, pady=10)
        self.reminder_entry.insert(INSERT, self.help)
        self.button1 = Button(master, text='CREATE NEW', width=25, command=self.new_post_it,
                              padx=5, pady=10)
        self.button1.pack()

    def new_post_it(self):
        
        N = 2

        date_N_days = datetime.now() + timedelta(days=N)
    
        newWindow = Toplevel(self.master)
        reminder_text = Label(newWindow, text=self.reminder_entry.get('1.0', END))
        reminder_text.pack()

        quit = Button(newWindow, text="QUIT", command=self.master.quit)
        quit.pack()

        self.postitems.append(reminder_text)

        if datetime.now() == date_N_days:
            for x in self.postitems:
                toaster = ToastNotifier()
                toaster.show_toast("Notification",
                                   self.reminder_entry.get("1.0", END),
                                   duration=6)

def main():        
    root = Tk()
    app = Create(root)
    root.mainloop()

if __name__ == "__main__":
    main()
