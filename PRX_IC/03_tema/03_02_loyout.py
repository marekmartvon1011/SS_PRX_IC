from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class app_03_02(App):
    def build(self):
        koren = BoxLayout(orientation = "vertical")
        koren.add_widget(Label(text = "Čauko"))
        koren.add_widget(Button(text = "Click"))
        return koren
        
app_03_02().run()
