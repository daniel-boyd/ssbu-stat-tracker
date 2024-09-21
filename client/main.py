from kivy.app import App
from .screens.character_select import CharacterSelectScreen

class App(App):
    def build(self):
        return CharacterSelectScreen()

if __name__ == '__main__':
    App().run()
