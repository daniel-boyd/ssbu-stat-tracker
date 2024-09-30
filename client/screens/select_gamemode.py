from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from .. import shared

Builder.load_file("client/layouts/select_gamemode.kv")

class SelectGameMode(MDScreen):
    def on_back_button_clicked(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'select_player_names'

    def standard_button_clicked(self):
        shared.set_current_match("game_mode_str", "standard")
        shared.set_current_format()
        self.manager.transition.direction = 'left'
        self.manager.current = 'select_character_mode'

    def handicap_button_clicked(self):
        shared.set_current_match("game_mode_str", "handicap")
        shared.set_current_format()
        self.manager.transition.direction = 'left'
        self.manager.current = 'select_character_mode'
