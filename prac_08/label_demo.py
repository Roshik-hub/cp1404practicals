from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class DynamicLabelsApp(App):
    def build(self):
        root = BoxLayout()
        main_box = root.ids.main
        names = ["Alice", "Bob", "Charlie", "Diana"]
        for name in names:
            main_box.add_widget(Label(text=name))
        return root

DynamicLabelsApp().run()
