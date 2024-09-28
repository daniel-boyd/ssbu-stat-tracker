from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from .screens.main_menu import MainMenu
from .screens.select_player_count import SelectPlayerCount
from .screens.character_select import CharacterSelectScreen

class SsbuStatTracker(MDApp):
    def build(self):
        Window.size = (1024, 600) 
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(SelectPlayerCount(name='select_player_count'))
        return sm

if __name__ == '__main__':
    SsbuStatTracker().run()
