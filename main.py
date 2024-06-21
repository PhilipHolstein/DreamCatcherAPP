import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.core.window import Window
from datetime import datetime
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.properties import NumericProperty, StringProperty
import json
import os

#bei versions problemen
#kivy.require("1.9.0")

currnetDreamView = StringProperty(0)

class WindowManager(ScreenManager):
    pass

class EntryWindow(Screen):
    date_time = StringProperty(0)

    def on_enter(self):
        now = datetime.now()
        self.date_time = now.strftime("%m/%d/%Y  %H:%M")

    def getFilename(self):
        now = datetime.now()
        return now.strftime("%m-%d-%Y")

    def saveFile(self, text):
        data = {"text":text, "datetime":self.date_time}
        with open("dreams/"+self.getFilename(), "w") as json_file:
            json.dump(data, json_file, indent=4)
        popup = Popup(title='Saving...', content=Label(text='your entry has been saved!'), size=(50, 50))
        popup.size_hint = (0.8, 0.2)
        popup.open()

class ListWindow(Screen):
    dreams = []


    def on_enter(self):
        self.dreams = []
        self.ids.dreamsList.clear_widgets()
        files = os.listdir("dreams/")
        start = 0
        i = 0
        for i in range(start, start+10):
            #maximal 10 Einträge anzeigen
            if(i>=len(files)):
                #add Empty Grid
                DreamColumn = GridLayout()
                DreamColumn.cols=1
                DreamColumn.size_hint = (1.0, 0.1)
                self.ids.dreamsList.add_widget(DreamColumn)
            else:
                file_name = files[i]
                self.dreams.append(file_name)
                DreamColumn = GridLayout()
                DreamColumn.cols=3
                DreamLabel = Label(text="Dream from "+file_name)
                DreamButtonView = Button(text="View")
                DreamButtonEdit = Button(text="Edit")
                DreamButtonView.background_color = (0.5, 0.7, 0.7, 0.7)
                DreamButtonEdit.background_color = (0.5, 0.7, 0.7, 0.7)
                DreamButtonEdit.size_hint = (0.15, 0.1)
                DreamButtonView.size_hint = (0.15, 0.1)
                DreamLabel.size_hint = (0.7, 0.1)
                DreamColumn.size_hint = (1.0, 0.1)
                DreamColumn.add_widget(DreamLabel)
                DreamColumn.add_widget(DreamButtonView)
                DreamColumn.add_widget(DreamButtonEdit)
                self.ids.dreamsList.add_widget(DreamColumn)
        print(self.dreams)
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