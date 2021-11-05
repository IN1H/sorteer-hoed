from tkinter import *


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
    ).place(x = eind_scherm.winfo_screenwidth() / 3, y = eind_scherm.winfo_screenmmheight() / 6)

    Label(eind_scherm,
        text =f"Voor de richting {User.get_max()} heb je {User.get_score()[User.get_index_of_max()]} punten",
        font=("Helvetica", 22),
        wraplength=700,
        justify="center"
    ).place(x = eind_scherm.winfo_screenwidth() / 3, y = eind_scherm.winfo_screenmmheight() / 3)

    eind_scherm.mainloop()
