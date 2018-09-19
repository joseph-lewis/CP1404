from kivy.app import App
from kivy.lang import Builder


MILES_TO_KM = 1.60934


class MilesConverter(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_calculate(self):
        miles = self.error_check()
        result = miles * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        try:
            input = float(self.root.ids.input_miles.text)
        except ValueError:
            input = 0
        input += change
        self.root.ids.input_miles.text = str(input)
        self.handle_calculate()
    def error_check(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0
MilesConverter().run()