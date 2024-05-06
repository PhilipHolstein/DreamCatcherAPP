import kivy
from kivy.app import App
from kivy.uix.label import Label

#bei versions problemen
#kivy.require("1.9.0")

class MainApp(App):
    
    def build(self):
        return Label(text="DreamCatcher")
    

myApp = MainApp()
myApp.run()