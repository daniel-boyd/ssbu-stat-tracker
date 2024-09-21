from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from views.counter_view import CounterView  # Import your view

class SSBUStatTrackerApp(App):
    def build(self):
        sm = ScreenManager()

        # Create an instance of StreakView
        counter_view = CounterView()

        # Create a screen for the view
        screen = Screen(name='counter')
        screen.add_widget(counter_view)

        # Add the screen to the screen manager
        sm.add_widget(screen)

        return sm

if __name__ == '__main__':
    SSBUStatTrackerApp().run()