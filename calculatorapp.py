from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Calculator(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = False
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=40,
            background_color=(0.29, 0.27, 0.32, 1),
            foreground_color=(1, 1, 1, 1),
        )
        main_layout.add_widget(self.solution)

        buttons = [
            ["1", "2", "3", "C"],
            ["4", "5", "6", "+"],
            ["7", "8", "9", "-"],
            ["=", "0", "÷", "×"],
        ]
        button_grid = GridLayout(cols=4, spacing=5)

        for row in buttons:
            for label in row:
                button = Button(
                    text=label,
                    font_size=32,
                    background_normal="",
                    background_color=self.get_button_color(label),
                    on_press=self.on_button_press,
                )
                button_grid.add_widget(button)

        main_layout.add_widget(button_grid)
        return main_layout

    def get_button_color(self, label):
        if label == "C":
            return (0.76, 0.29, 0.21, 1)
        elif label == "=":
            return (0.43, 0.29, 0.56, 1)
        else:
            return (0.29, 0.27, 0.32, 1)

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        elif button_text == "=":
            try:
                expression = current.replace("×", "*").replace("÷", "/")
                self.solution.text = str(eval(expression))
            except Exception:
                self.solution.text = "Fehler"
        else:
            if current == "Fehler":
                current = ""
            self.solution.text = current + button_text

if __name__ == "__main__":
    Calculator().run()