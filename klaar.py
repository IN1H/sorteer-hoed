from tkinter import *
from tkinter import ttk



def eind_resultaat(richting):
    if richting == "IAT":
        return "De richting interactie technologie ligt jou het meeste!"

    if richting == "BDAM":
        return "De richting buisness data management ligt jou het meeste!"
        
    if richting == "SE":
        return "De richting software engeineering ligt jou het meeste!"
        
    if richting == "FICT":
        return "De richting forensische ICT ligt jou het meeste!"

    if richting == "niks":
        return "De richting Toverschool ligt jou het meeste!"

def eind_scherm_func(User):


    eind_scherm = Tk()
    eind_scherm.geometry("800x600")
    eind_scherm.state("zoomed")
    eind_scherm.title("IN1H - sorteerhoed")
    eind_scherm.iconbitmap("assets/icon.ico")
    
    Label(eind_scherm,
        text =eind_resultaat(User.get_max()),
        font=("Helvetica", 22),
        wraplength=700,
        justify="center"
    ).place(x = eind_scherm.winfo_screenwidth() / 3, y = 100)

    Label(eind_scherm,
        text =f"Voor de richting {User.get_max()} heb je {User.get_score()[User.get_index_of_max()]} punten.",
        font=("Helvetica", 22),
        wraplength=700,
        justify="center"
    ).place(x = eind_scherm.winfo_screenwidth() / 2.7, y =300 )

    style = ttk.Style()
    style.configure("Custom.TLabel", background="#ececec", foreground="#000", font="Ariel 16 bold")
    style.configure("Custom.TButton", activebackground="#d9d9d9", fg="black", font="Ariel 16 bold")
    style.configure("Custom.TRadiobutton", background="#ececec", foreground="#000", font="Ariel 14", wraplength=600, justify="left")


    btn = ttk.Button(eind_scherm, text ="Afsluiten", command = eind_scherm.destroy, width = 10, style="Custom.TButton")
    btn.grid(pady = 1, row=3, columnspan=4)
    btn.place(x = eind_scherm.winfo_screenwidth() / 2.2, y = 400)

    eind_scherm.mainloop()
