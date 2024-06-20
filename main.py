import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from datetime import datetime
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.properties import NumericProperty, StringProperty
import json

#bei versions problemen
#kivy.require("1.9.0")

class WindowManager(ScreenManager):
    pass

class EntryWindow(Screen):
    date_time = StringProperty(0)

    def on_enter(self):
        now = datetime.now()
        self.date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    
    def getFilename(self):
        now = datetime.now()
        return now.strftime("%m-%d-%Y")

    def saveFile(self, text):
        data = {"text":text, "datetime":self.date_time}
        with open("dreams/"+self.getFilename(), "w") as json_file:
            json.dump(data, json_file, indent=4)

class ListWindow(Screen):
    pass

kv = Builder.load_file("Screens.kv")
class MainApp(App):
    
    def build(self):
        #window
        #Window.size = (300, 100)
        return kv

    
    def deleteAll(self, instance):
        self.textfield.text = ""

    

myApp = MainApp()
myApp.run()