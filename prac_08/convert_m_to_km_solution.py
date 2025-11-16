from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder


MILES_TO_KM = 1.60934

class ConvertMilesKmApp(App):
    km_text = StringProperty('0.0')

    def handle_convert(self):
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0.0
        self.km_text = f"{miles * MILES_TO_KM:.2f}"

    def handle_increment(self, value):
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0.0
        miles += value
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

if __name__ == '__main__':
    ConvertMilesKmApp().run()
