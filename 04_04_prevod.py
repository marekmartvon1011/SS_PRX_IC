from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class mojaApka(App):
    def build(self):
        plocha = BoxLayout(orientation = "vertical")
        
        in_out = BoxLayout()
        self.input = TextInput(hint_text = "zadaj cm", multiline = False)
        self.output = Label(text = " ")
        in_out.add_widget(self.input)
        in_out.add_widget(self.output)
        
        plocha.add_widget(in_out)
        return plocha
    
    def klik(self,kto_zavolala):
        
        
mojaApka().run()