from kivy.core.window import Window
from kivymd.app import MDApp
from .screens.character_select import CharacterSelectScreen
from .screens.main_menu import MainMenu

class SsbuStatTracker(MDApp):
    def build(self):
        Window.size = (1024, 600) 
        self.theme_cls.theme_style = "Dark"
        return MainMenu()

if __name__ == '__main__':
    SsbuStatTracker().run()
