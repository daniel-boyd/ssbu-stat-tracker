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
from .screens.select_bot import SelectBot
from .screens.select_player_character import SelectPlayerCharacter
from .screens.select_player_character_3p import SelectPlayerCharacter3p
from .screens.stage_list import StageList
from .screens.match import Match
from .screens.set_player_stats import SetPlayerStats
from .screens.post_game_stats_screen import PostGameStatsScreen
from . import shared

# Character buttons in select_character.kv call this function, which determines the current
# active screen and calls the appropriate function from that screen
class SSBUScreenManager(ScreenManager):
    def handle_character_button_press(self, button):
        if shared.get_current_match_value_from_key("num_players_str") == "3p":
            self.get_screen("select_player_character_3p").on_character_button_pressed(button)
        else:
            self.get_screen("select_player_character").on_character_button_pressed(button)


class SsbuStatTracker(MDApp):
    def build(self):
        Window.size = (1024, 600) 
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        sm = SSBUScreenManager()
        
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(SelectPlayerCount(name='select_player_count'))
        sm.add_widget(SelectPlayerNames(name='select_player_names'))
        sm.add_widget(SelectGameMode(name='select_gamemode'))
        sm.add_widget(SelectCharacterMode(name='select_character_mode'))
        sm.add_widget(SelectCharacter(name='select_character'))
        sm.add_widget(SelectPlayerCharacter(name='select_player_character'))
        sm.add_widget(SelectPlayerCharacter3p(name='select_player_character_3p'))
        sm.add_widget(Match(name='match'))
        sm.add_widget(SetPlayerStats(name='set_player_stats'))
        sm.add_widget(SelectBot(name='select_bot'))
        sm.add_widget(StageList(name='stage_list'))
        sm.add_widget(PostGameStatsScreen(name='post_game_stats_screen'))
        return sm

if __name__ == '__main__':
    SsbuStatTracker().run()
