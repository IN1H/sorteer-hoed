# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from db import Database
from app import App
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

# creates a Tk() object
from playSound import play

master = Tk()

# sets the geometry of main
# root window
master.geometry("800x600")
master.state("zoomed")

screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()

# master.attributes('-fullscreen', True)
 
 
# function to open a new window
# on a button click
def openNewWindow():
    master.destroy()
    gui = Tk()

    # # Easter egg code die geactiveerd wordt met de "h" toets.
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
    style.configure("Custom.TRadiobutton", background="#ececec", foreground="#000", font="Ariel 14", wraplength=600,
                    justify="left")

    # View configuratie.
    gui.geometry(f"{screen_width}x{screen_height}")
    gui.configure(bg="#ececec")
    gui.state("zoomed")
    gui.title("IN1H - sorteerhoed")
    gui.iconbitmap("assets/icon.ico")

    # Event voor de easter egg.
    gui.bind('<Key>', key)

    # Verkrijg de data van de database.

    # Maak de app.
    app = App(gui)
    
 
 
appTitle = Label(master,
              text ="Welkom bij Team Trampoline's Informatica sorteer hoed quiz",
              font=("Helvetica", 22),
              wraplength=700,
              justify="center")

y_pos = screen_height / 6
appTitle.grid(pady = 10, row=0, columnspan=4)
appTitle.place(x = screen_width / 3, y = y_pos)

appDesc = Label(master,
              text =f"Deze quiz is bedoeld om voor jou te bepalen welke van de 4 mogelijke Informatica richtingen het beste voor jou geschikt zijn. Er worden {len(Database().get_all())} vragen gesteld, en je antwoorden bepalen je meest geschikte richting(en).",
              font=("Helvetica", 16),
              wraplength=600,
              justify="center")

y_pos = screen_height / 4
appDesc.grid(pady = 20, row=1, columnspan=4)
appDesc.place(x = screen_width / 3, y = y_pos)

# Display [richting] icon
getImg1 = Image.open("img/img1.png")
resizeImg1 = getImg1.resize((200, 200))
img1 = ImageTk.PhotoImage(resizeImg1)

y_pos = screen_height / 3
y_pos += 50
x_pos = screen_width / 4
img1Label = Label(image=img1)
img1Label.image = img1
img1Label.grid(column=0, row=2)
img1Label.place(x = x_pos, y = y_pos)

# Display [richting] icon
img2 = ImageTk.PhotoImage(Image.open("img/img2.png").resize((200, 200)))

x_pos += screen_width / 8
img2Label = Label(image=img2).image = img2
img2Label.grid(column=1, row=2)
img2Label.place(x = x_pos, y = y_pos)

# Display [richting] icon
img3 = ImageTk.PhotoImage(Image.open("img/img3.png").resize((200, 200)))

x_pos += screen_width / 7
img3Label = Label(image=img3)
img3Label.image = img3
img3Label.grid(column=2, row=2)
img3Label.place(x = x_pos, y = y_pos)

# Display [richting] icon
getImg4 = Image.open("img/img4.png")
resizeImg4 = getImg4.resize((200, 200))
img4 = ImageTk.PhotoImage(resizeImg4)

x_pos += screen_width / 8
img4Label = Label(image=img4)
img4Label.image = img4
img4Label.grid(column=3, row=2)
img4Label.place(x = x_pos, y = y_pos)

# a button widget which will open a
# new window on button click
y_pos = screen_height / 1.5
master.title("IN1H - sorteerhoed")
master.iconbitmap("assets/icon.ico")
btn = Button(master,
             text ="Start",
             command = openNewWindow)
btn.grid(pady = 1, row=3, columnspan=4)
btn.place(x = screen_width / 2, y = y_pos)
 
# mainloop, runs infinitely
master.mainloop()