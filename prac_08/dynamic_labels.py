from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Load the KV file
Builder.load_file('dynamic_labels.kv')

class RootWidget(BoxLayout):
    pass

class DynamicLabelsApp(App):
    def build(self):
        return RootWidget()

    def add_label(self):
        # Get the text from TextInput
        text = self.root.ids.input_text.text
        if text.strip():
            from kivy.uix.label import Label
            new_label = Label(
                text=text,
                color=(0, 0, 0, 1),
                size_hint_y=None,
                height=30
            )
            self.root.ids.labels_box.add_widget(new_label)
            self.root.ids.input_text.text = ''

if __name__ == '__main__':
    DynamicLabelsApp().run()
