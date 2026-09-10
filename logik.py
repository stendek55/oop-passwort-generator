import secrets
import string

class PasswortGenerator:

    #konstanten für zeichenvorräte
    KLEIN_BSTABE  = string.ascii_lowercase
    GROSS_BSTABE  = string.ascii_uppercase
    ZAHLEN        = string.digits
    SONDER_ZEICHN = string.punctuation

    #konstruktor
    def __init__(self, laenge):
        #passwortlänge
        self.pw_laenge = int(laenge)
        #zeichenvorrat die im pw enthalten sein sollen
        self.passwort_vorrat = []

        #liste für gewählte zeichen die ins pw kommen
        self.passwort_zeichen = []

        #endgültiges passwort
        self.passwort_final = ""


    #zeichenvorrat mit kleinen buchstaben auffüllen 
    def set_klein_buchstaben(self):
        #ein element zufällig auswählen
        #damit auch garantiert ist das mindest einmal dieses zeichen im pw enthalten ist
        self.passwort_zeichen += secrets.choice(self.KLEIN_BSTABE)
        #den zeichenvorrat mit allen kleinen buchstaben hinzufügen
        self.passwort_vorrat.extend(self.KLEIN_BSTABE)
        return None
    

    #zeichenvorrat mit grossen buchstaben auffüllen 
    def set_gross_buchstaben(self):
        self.passwort_zeichen += secrets.choice(self.GROSS_BSTABE)
        self.passwort_vorrat.extend(self.GROSS_BSTABE)
        return None
    

    #zeichenvorrat mit zahlen auffüllen 
    def set_zahlen(self):
        self.passwort_zeichen += secrets.choice(self.ZAHLEN)
        self.passwort_vorrat.extend(self.ZAHLEN)
        return None
    

    #zeichenvorrat mit sonderzeichen auffüllen 
    def set_sonder_zeichen(self):
        self.passwort_zeichen += secrets.choice(self.SONDER_ZEICHN)
        self.passwort_vorrat.extend(self.SONDER_ZEICHN)
        return None
    

    #pw wird mit der vorgegeben länge aus dem zeichenvorrat aufgefüllt
    def pw_auffuellen(self):
        #anzahl der zeichen die vorkommen müssen
        sum_zeichen = len(self.passwort_zeichen)

        for _ in range(sum_zeichen, self.pw_laenge):
            self.passwort_zeichen += secrets.choice(self.passwort_vorrat)

    
    #alle enthaltenen zeichen nochmals mischen um sicherheit zu erhöhen
    def pw_schuetteln(self):
        #self.passwort_final = "".join(secrets.SystemRandom().sample(self.passwort_zeichen, len(self.passwort_zeichen)))
        mischer = secrets.SystemRandom()
        mischer.shuffle(self.passwort_zeichen)
        self.passwort_final = "".join(self.passwort_zeichen)


    #der getter fürs finale pw
    @property
    def passwort(self):
        #auffüllen
        self.pw_auffuellen()
        #mischen
        self.pw_schuetteln()

        #zurückgeben
        return self.passwort_final