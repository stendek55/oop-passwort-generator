import customtkinter as ctk
from logik import PasswortGenerator

#grundeinstellungen für das modernes design
ctk.set_appearance_mode("dark")  # Modi: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue") # Themen: "blue" (standard), "green", "dark-blue"

class ModernApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Fenster-Konfiguration
        # Setzt den Text, der ganz oben in der Titelleiste des Fensters angezeigt wird
        self.title("Passwortgenerator_0.1")
        # Bestimmt die Startgröße des Fensters beim Öffnen (Breite x Höhe in Pixeln)
        self.geometry("333x400")

        # Layout-Raster konfigurieren
        # Konfiguriert das unsichtbare Gitternetz (Grid) des Fensters.
        # - 0: Betrifft die erste Spalte (Spalte 0).
        # - weight=1: Die Spalte verhält sich "elastisch". Wenn das Fenster vergrößert wird,
        #   dehnt sich diese Spalte automatisch aus und nimmt den freien Platz ein.
        self.grid_columnconfigure(0, weight=1)

        # === CHECKBOX-ELEMENTE ===        
        # Erstellt das eigentliche Steuerelement (Widget) für die Checkbox.
        self.checkbox_klein = ctk.CTkCheckBox(
            self,                           # 'self' bedeutet: Die Checkbox wird direkt in das Hauptfenster gepackt
            text="kleinbuchstaben",         # Der Beschriftungstext rechts neben dem Auswahl-Quadrat
            corner_radius=5,                # Bestimmt, wie stark die Ecken des Auswahl-Quadrats abgerundet sind (in Pixeln)
            checkbox_width=24,              # Die Breite des anklickbaren Auswahl-Quadrats (in Pixeln)
            checkbox_height=24              # Die Höhe des anklickbaren Auswahl-Quadrats (in Pixeln)
        )

        # --- PLATZIERUNG IM FENSTER ---        
        # Positioniert das fertige Checkbox-Element mithilfe des Gitternetzes (Grid).
        self.checkbox_klein.grid(
            row=1,                          # Setzt das Element in die zweite Zeile (Achtung: Gitternetze fangen bei 0 an!)
            column=0,                       # Setzt das Element in die erste Spalte (Spalte 0)
            
            # padx = Außenabstand nach links und rechts:
            # - 60: Lässt links vom Element einen großzügigen Freiraum von 60 Pixeln (schiebt es nach rechts)
            padx=60, 
            
            # pady = Außenabstand nach oben und unten:
            # - (23, 10) ist ein spezielles Tuple: 23 Pixel Abstand nach oben, 10 Pixel Abstand nach unten
            pady=(23, 10), 
            
            # sticky = Ausrichtung innerhalb der Gitterzelle:
            # - "w" steht für "Westen" (links). Das sorgt dafür, dass das Element linksbündig ausgerichtet wird,
            #   selbst wenn die Spalte im Hintergrund breiter ist als das Element selbst.
            sticky="w"
        )

        self.checkbox_gross = ctk.CTkCheckBox(self, 
                                        text="GROSSBUCHSTABEN",
                                        corner_radius=5,    
                                        checkbox_width=24,  
                                        checkbox_height=24)
        self.checkbox_gross.grid(row=2, column=0, padx=60, pady=10, sticky="w")

        self.checkbox_zahlen = ctk.CTkCheckBox(self, 
                                        text="zahl3n",
                                        corner_radius=5,    
                                        checkbox_width=24,  
                                        checkbox_height=24)
        self.checkbox_zahlen.grid(row=3, column=0, padx=60, pady=10, sticky="w")

        self.checkbox_sonder = ctk.CTkCheckBox(self, 
                                        text="$onderzeichen",
                                        corner_radius=5,    
                                        checkbox_width=24,  
                                        checkbox_height=24)
        self.checkbox_sonder.grid(row=4, column=0, padx=60, pady=10, sticky="w")

        # === DROPDOWN ===        
        #liste mit werten erzeugen die in dropdown menu kommen
        optionen_liste = [str(i) for i in range(12, 25)]

        self.auswahl = ctk.CTkOptionMenu(self, 
                                        values=optionen_liste,
                                        width=222,
                                        height=35,
                                        corner_radius=10)
        self.auswahl.grid(row=5, column=0, padx=(60, 20), pady=10, sticky="w")

        # Optional: Einen Standardwert setzen
        self.auswahl.set("???PW länge???") 

        # === BUTTON ===        
        self.button = ctk.CTkButton(self, 
                                    text="PW generieren",
                                    width=222,
                                    height=40,
                                    corner_radius=10,
                                    font=ctk.CTkFont(size=15, weight="bold"),
                                    command=self.button_event)
        self.button.grid(row=6, column=0, padx=(60, 20), pady=10, sticky="w")

        # === AUSGABEFELD ===        
        self.output_entry = ctk.CTkEntry(self, 
                                        width=222, 
                                        height=35,
                                        corner_radius=10,
                                        border_width=2)
        self.output_entry.grid(row=7, column=0, padx=(60, 20), pady=10, sticky="w")

        # Text setzen
        self.output_entry.insert(0, "...")


    def label_ausgabe(self, nachricht):
        self.output_entry.configure(state="normal")
        self.output_entry.delete(0, "end")
        self.output_entry.insert(0, nachricht)
        # Auf Schreibgeschützt setzen (Markieren & Kopieren bleibt erlaubt)
        self.output_entry.configure(state="readonly")


    def button_event(self):

        #abfangen wenn keine länge ausgewählt
        if self.auswahl.get() == "???PW länge???":
            self.label_ausgabe("!!!PW länge WÄHLEN!!!")
            return
        
        #abfangen wenn keine zeichenvorräte geclickt
        if (self.checkbox_zahlen.get() == 0 
                and self.checkbox_klein.get() == 0 
                and self.checkbox_gross.get() == 0 
                and self.checkbox_sonder.get() == 0):

            self.label_ausgabe("!!!zeichenvorrat WÄHLEN!!!")
            return

        #objekt erstellen
        pass_wort = PasswortGenerator(self.auswahl.get())

        #prüfen welche checkboxen aktiviert wurden 
        #und entsprechenden zeichenvorrat setzen
        if self.checkbox_zahlen.get() == 1:
            pass_wort.set_zahlen()
        if self.checkbox_klein.get() == 1:
            pass_wort.set_klein_buchstaben()
        if self.checkbox_gross.get() == 1:
            pass_wort.set_gross_buchstaben()
        if self.checkbox_sonder.get() == 1:
            pass_wort.set_sonder_zeichen() 

        #generierung und ausgabe des erstellten pw
        self.label_ausgabe(pass_wort.passwort)
         
        
if __name__ == "__main__":
    app = ModernApp()
    app.mainloop()
