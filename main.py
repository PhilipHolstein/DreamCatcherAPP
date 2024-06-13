import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from datetime import datetime


#bei versions problemen
#kivy.require("1.9.0")

class MainApp(App):
    
    def build(self):
        #window
        #Window.size = (300, 100)

        #grid
        window = GridLayout()
        window.cols = 1
        window.size_hint = (1, 1)
        window.pos_hint = {"center_x":0.5, "center_y":0.5}

        #date
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        date = Label(text=date_time)
        date.size_hint = (1, 0.2)
        window.add_widget(date)

        #textfield
        textfield = TextInput(multiline=True, padding= (10, 0, 10, 0))
        textfield.size_hint = (1, 1)
        #textfield.padding= (10, 0, 10, 0)
        window.add_widget(textfield)

        #buttonfield
        buttonfield = GridLayout()
        buttonfield.cols = 2
        buttonfield.size_hint = (1, 0.2)




        #buttons
        deletebutton = Button(text="delete")
        buttonfield.add_widget(deletebutton)
        finishbutton = Button(text="finish")
        buttonfield.add_widget(finishbutton)

        window.add_widget(buttonfield)


        return window
    

myApp = MainApp()
myApp.run()