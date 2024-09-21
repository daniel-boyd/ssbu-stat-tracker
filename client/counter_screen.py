from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text='Counter: 0')
        self.add_widget(self.label)

        self.increment_button = Button(text='Increment Counter')
        self.increment_button.bind(on_press=self.increment_counter)
        self.add_widget(self.increment_button)

    def increment_counter(self, instance):
        current_counter = int(self.label.text.split(': ')[1])
        self.label.text = f'Counter: {current_counter + 1}'