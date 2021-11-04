from db import Database
from klaar import eind_resultaat
from playSound import play
from user import User
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

user = User()

class App():

    # Initialiseren van de class
    def __init__(self):

        # Huidige vraag nummer (Begint bij 0)
        self.q_no=0
         
        # Maak een nieuwe user voor de app.
        self.User = User()

        # sla de scherm resolutie op.
        self.screen_width = gui.winfo_screenwidth()
        self.screen_height = gui.winfo_screenheight()

        # Vraag label
        self.question_label = ttk.Label(gui, text="", width=70, wraplength=750, justify="left", style="Custom.TLabel", anchor= 'w' )
        self.question_label.place(x=self.screen_width/4, y=self.screen_height/3 - 80)

        # Laat de vraag zien.
        self.display_question()
         
        # Variabel waar het opgegeven antwoord in wordt opgeslagen.
        self.opt_selected=IntVar()
         
        # Plaats alle antwoord mogelijkheden in het scherm.
        self.opts=self.radio_buttons()
        
        # Laat de antwoord mogelijkheden zien.
        self.display_options()
        
        # laat de volgende en stop knop zien in het scherm.
        self.buttons()
        
        # De lengte van de quiz.
        self.data_size=len(data)

    # Volgende knop  
    def volgende_knop(self):

        # Als de index van het geslecteerde antwoord groter dan 0 is is er een antwoord gegeven.
        if self.opt_selected.get() > 0:

            # Stop de punten indeling van het huidige antwoord in een variabele.
            punten = data[self.q_no]["Answers"][(self.opt_selected.get()-1)]

            # Voeg aan de gebruiker de punten voor elke richting toe.
            self.User.add_bdam(punten["BDAM"]).add_fict(punten["FICT"]).add_iat(punten["IAT"]).add_se(punten["SE"]).add_niks(punten["niks"])

            # Verhoog de vraag index.
            self.q_no += 1

            # Loop over de antwoorden en verwijder deze van het scherm.
            i=0
            for opt in self.opts:
                self.opts[i].destroy()
                i +=1

            # Reset de antwoorden en maak de nieuwe aan
            self.opts.clear()
            self.opts = self.radio_buttons()

            # Als op de laatste vraag antwoord is gegeven, laat de uitslag zien en vernietig de gui.
            if self.q_no == self.data_size:
                gui.destroy()
                messagebox.showinfo("Klaar!",eind_resultaat(self.User.get_max()))
             
            # Render de vraag en antwoorden.
            else:
                self.display_question()
                self.display_options()
        
        # Laat een bericht zien dat de gebruiker niks heeft ingevuld.
        else:
            messagebox.showinfo("fout", "Selecteer een antwoord!")

    # Laat de volgende & stop knop zien.
    def buttons(self):
        
        # Maak de volgende knop
        next_button = ttk.Button(gui, text="Volgende",command=self.volgende_knop,
        width=10,style="Custom.TButton")
         
        # Plaats de volgende knop
        next_button.place(x=self.screen_width/4,y=screen_height/3 + 320)
         
        # Maak de stop knop
        quit_button = ttk.Button(gui, text="Afsluiten", command=gui.destroy, width=10,style="Custom.TButton")

        # Plaats de stop knop
        quit_button.place(x=self.screen_width - 140, y=self.screen_height - 160)

         
    # Laat alle antwoord opties zien.
    def display_options(self):
        val=0

        self.opt_selected.set(0)

        # Voeg de antwoorden toe aan de huidige antwoord lijst.
        for option in options[self.q_no]['Answers']:
            self.opts[val]['text']=option['answer']
            val+=1


        # Verwijder de lege antwoorden.
        if val == 2:
            self.opts[2].destroy()
            self.opts[3].destroy()
            self.opts[4].destroy()
        if val == 3:
            self.opts[3].destroy()
            self.opts[4].destroy()
        if val == 4:
            self.opts[4].destroy()

    # Laat de vraag zien
    def display_question(self):

        # Stel de label op de huidige vraag van de database in.
        self.question_label['text'] = f"Vraag {self.q_no + 1}: {question[self.q_no]['question']}"

    # Laat de antwoord knoppen zien.
    def radio_buttons(self):
         
        q_list = []
        
        # De positie van de antwoord knoppen
        y_pos = self.screen_height / 3
        
        # Radiobutton while loop to display all options for each question
        while len(q_list) < 5:
             
            radio_btn = ttk.Radiobutton(gui,text=" ",variable=self.opt_selected, value = len(q_list)+1,style="Custom.TRadiobutton")
             
            q_list.append(radio_btn)
             
            radio_btn.place(x = self.screen_width / 4, y = y_pos)
             
            y_pos += 60
            
        return q_list

# maak de GUI Window

gui = Tk()

# Easter egg
def key(event):
    if event.char == "h":
        play()

# Screen width & height
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()

# Standard styling
style = ttk.Style()
style.configure("Custom.TLabel", background="#ececec", foreground="#000", font="Ariel 16 bold")
style.configure("Custom.TButton", activebackground="#d9d9d9", fg="black", font="Ariel 16 bold")
style.configure("Custom.TRadiobutton", background="#ececec", foreground="#000", font="Ariel 14", wraplength=600, justify="left")

# View config
gui.geometry(f"{screen_width}x{screen_height}")
gui.configure(bg="#ececec")
gui.state("zoomed")
gui.title("IN1H - sorteerhoed")
gui.iconbitmap("assets/icon.ico")

# Event voor de easter egg.
gui.bind('<Key>', key)
 
# Verkrijg de data van de database.
data = Database().get_all()
question, options = data, data

# Maak de app.
app = App()
 
# Start the GUI
gui.mainloop()
