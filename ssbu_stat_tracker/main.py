from kivy.app import App
from kivy.uix.label import Label

class SSBUStatTrackerApp(App):
    def build(self):
        return Label(text="Welcome to SSBU Stat Tracker!")

if __name__ == "__main__":
    SSBUStatTrackerApp().run()