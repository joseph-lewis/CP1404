from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class SimpleApp(App):

    def build(self):
        names = ["Joe", "Tim", "Bob", "George"]
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        for name in names:
            temp_button = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_button)
        return self.root


SimpleApp().run()