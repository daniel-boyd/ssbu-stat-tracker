import datetime
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from .screens.main_menu import MainMenu
from .screens.select_player_count import SelectPlayerCount
from .screens.select_player_names import SelectPlayerNames
from .screens.select_gamemode import SelectGameMode
from .screens.select_character_mode import SelectCharacterMode
from .screens.select_character import SelectCharacter
from .screens.select_player_character import SelectPlayerCharacter
from .screens.stage_list import StageList
from .screens.match import Match

class SsbuStatTracker(MDApp):
    def build(self):
        Window.size = (1024, 600) 
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.theme_style = "Dark"
        sm = ScreenManager()
        sm.add_widget(Match(name='match'))
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(SelectPlayerCount(name='select_player_count'))
        sm.add_widget(SelectPlayerNames(name='select_player_names'))
        sm.add_widget(SelectGameMode(name='select_gamemode'))
        sm.add_widget(SelectCharacterMode(name='select_character_mode'))
        sm.add_widget(SelectCharacter(name='select_character'))
        sm.add_widget(SelectPlayerCharacter(name='select_player_character'))
        sm.add_widget(StageList(name='stage_list'))
        return sm

if __name__ == '__main__':
    SsbuStatTracker().run()
