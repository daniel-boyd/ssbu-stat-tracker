from kivy.app import App
from .screens.counter_screen import CounterScreen

class CounterApp(App):
    def build(self):
        return CounterScreen()

if __name__ == '__main__':
    CounterApp().run()
