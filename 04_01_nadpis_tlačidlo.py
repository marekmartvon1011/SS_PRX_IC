from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class mojaApka(App):
    def build(self):
        plocha = BoxLayout(orientation='vertical')
        plocha.add_widget(Label(text="Ano", color = (1,0,0,1)))
        plocha.add_widget(Button(text="1"))

        return plocha
    
mojaApka().run()
