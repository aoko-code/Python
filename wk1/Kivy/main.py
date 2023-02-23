import Kivy
from kivy.app import App
from Kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 1)
#create layout class
class CalcLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = 'Error'

class CalcApp(App):
    def build(self):
        return CalcLayout()

calculatorApp = CalcApp()
calculatorApp.run()
