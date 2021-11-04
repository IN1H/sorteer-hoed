#Import tkinter library
from tkinter import *
from tkinter import ttk

from main import App
#Create an instance of tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
#Define a new function to open the window
def open_win():
    
    win.withdraw()
    gui = Toplevel(win)
    
    # Easter egg code die geactiveerd wordt met de "h" toets.
    def key(event):
        if event.char == "h":
            play()

    # Scherm breedte & hoogte.
    screen_width = gui.winfo_screenwidth()
    screen_height = gui.winfo_screenheight()

    # Standaard styling configuraties.
    style = ttk.Style()
    style.configure("Custom.TLabel", background="#ececec", foreground="#000", font="Ariel 16 bold")
    style.configure("Custom.TButton", activebackground="#d9d9d9", fg="black", font="Ariel 16 bold")
    style.configure("Custom.TRadiobutton", background="#ececec", foreground="#000", font="Ariel 14", wraplength=600, justify="left")

    # View configuratie.
    gui.geometry(f"{screen_width}x{screen_height}")
    gui.configure(bg="#ececec")
    gui.state("zoomed")
    gui.title("IN1H - sorteerhoed")
    gui.iconbitmap("assets/icon.ico")

    # Event voor de easter egg.
    gui.bind('<Key>', key)
    # Maak de app.
    app = App()

#Create a label
Label(win, text= "Click the below button to Open a New Window", font= ('Helvetica 17 bold')).pack(pady=30)
#Create a button to open a New Window
ttk.Button(win, text="Open", command=open_win).pack()
win.mainloop()