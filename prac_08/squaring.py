from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class SquaringApp(App):
    result_text = StringProperty('0')

    def handle_calculate(self):
        try:
            num = int(self.root.ids.input_number.text)
            self.result_text = str(num ** 2)
        except ValueError:
            self.result_text = '0'

if __name__ == '__main__':
    SquaringApp().run()
