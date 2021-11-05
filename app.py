from db import Database
from klaar import eind_resultaat, eind_scherm_func
from playSound import play
from user import User
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

user = User()

class App():

    # Initialiseren van de class
    def __init__(self, gui):
        self.gui = gui

        self.data = Database().get_all()

        # Huidige vraag nummer (Begint bij 0)
        self.q_no=0
         
        # Maak een nieuwe user voor de app.
        self.User = User()

        # sla de scherm resolutie op.
        self.screen_width = self.gui.winfo_screenwidth()
        self.screen_height = self.gui.winfo_screenheight()

        # Vraag label
        self.question_label = ttk.Label(self.gui, text="", width=70, wraplength=750, justify="left", style="Custom.TLabel", anchor= 'w' )
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
        self.data_size=len(self.data)

    # Volgende knop  
    def volgende_knop(self):

        # Als de index van het geslecteerde antwoord groter dan 0 is is er een antwoord gegeven.
        if self.opt_selected.get() > 0:

            # Stop de punten indeling van het huidige antwoord in een variabele.
            punten = self.data[self.q_no]["Answers"][(self.opt_selected.get()-1)]

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
                self.gui.destroy()

                eind_scherm = Tk()
                eind_scherm.geometry(f"{self.screen_width}x{self.screen_height}")
                eind_scherm.state("zoomed")
                eind_scherm.title("IN1H - sorteerhoed")
                eind_scherm.iconbitmap("assets/icon.ico")
                
                Label(eind_scherm,
                    text =eind_resultaat(self.User.get_max()),
                    font=("Helvetica", 22),
                    wraplength=700,
                    justify="center"
                ).pack()

                eind_scherm.mainloop()
                eind_scherm_func(self.User)

             
            # Render de vraag en antwoorden.
            else:
                self.display_question()
                self.display_options()
        
        # Laat een bericht zien dat de gebruiker niks heeft ingevuld.
        else:
            messagebox.showinfo("Info", "Je mag niet niks selecteren, selecteer een antwoord.")

    # Laat de volgende & stop knop zien.
    def buttons(self):
        
        # Maak de volgende knop
        next_button = ttk.Button(self.gui, text="Volgende",command=self.volgende_knop,
        width=10,style="Custom.TButton")
         
        # Plaats de volgende knop
        next_button.place(x=self.screen_width/4,y=self.screen_height/3 + 320)
         
        # Maak de stop knop
        quit_button = ttk.Button(self.gui, text="Afsluiten", command=self.gui.destroy, width=10,style="Custom.TButton")

        # Plaats de stop knop
        quit_button.place(x=10,y=10)

         
    # Laat alle antwoord opties zien.
    def display_options(self):
        val=0

        self.opt_selected.set(0)

        # Voeg de antwoorden toe aan de huidige antwoord lijst.
        for option in self.data[self.q_no]['Answers']:
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

    # Laat de vraag zien.
    def display_question(self):

        # Stel de label op de huidige vraag van de database in.
        self.question_label['text'] = f"Vraag {self.q_no + 1}: {self.data[self.q_no]['question']}"

    # Laat de antwoord knoppen zien.
    def radio_buttons(self):
         
        q_list = []
        
        # De positie van de antwoord knoppen.
        y_pos = self.screen_height / 3
        
        # Radiobutton while loop om alle opties voor de vragen te laten zien.
        while len(q_list) < 5:
            
            # Radiobutton styling.
            radio_btn = ttk.Radiobutton(self.gui,text=" ",variable=self.opt_selected, value = len(q_list)+1,style="Custom.TRadiobutton")
             
            q_list.append(radio_btn)
            
            # Radiobutton positionering.
            radio_btn.place(x = self.screen_width / 4, y = y_pos)
             
            y_pos += 60
            
        return q_list