from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class mojaApka(App):
    def build(self):
        plocha = BoxLayout(orientation = "vertical")
        
        self.pocet_klikov = 0
        self.popisok = Label(text = f"zatial nic {self.pocet_klikov} kliknuti")
        plocha.add_widget(self.popisok)
        
        tlacidlo = Button(text = "klikni na mna")
        tlacidlo.bind(on_release = self.klik)
        plocha.add_widget(tlacidlo)
        
        return plocha
    
    def klik(self,kto_zavolala):
        self.pocet_klikov += 1
        self.popisok.text = f"Marek, klikla si {self.pocet_klikov}-krát"
        
        
mojaApka().run()