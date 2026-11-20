from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class mojaApka(App):
    def build(self):
        tlacidlo = Button(text = "Klikni ma")
        tlacidlo.bind(on_press = self.klik)
        return tlacidlo
    
    def klik(self,kto_zavolal):
        print("niekto na mna klikol")
    
mojaApka().run()
