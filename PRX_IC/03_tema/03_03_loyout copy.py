from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class app_03_03(App):
    def build(self):
        koren = GridLayout(cols = 2, rows = 3)  
        koren.add_widget(Button(text = "A"))
        koren.add_widget(Button(text = "B"))
        koren.add_widget(Button(text = "C"))
        koren.add_widget(Button(text = "D"))
        koren.add_widget(Button(text = "E"))
        koren.add_widget(Button(text = "F"))
        return koren
        
app_03_03().run()
