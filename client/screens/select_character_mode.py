from .. import shared
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file("client/layouts/select_character_mode.kv")

class SelectCharacterMode(MDScreen):
    def on_back_button_clicked(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'select_gamemode'

    def pick_button_clicked(self):
        shared.set_current_match("character_mode_str", "pick")
        shared.set_current_format()
        self.manager.transition.direction = 'left'
        if shared.get_current_match_value_from_key("num_players_str") == "3p":
            self.manager.current = 'select_player_character_3p'
        else:
            self.manager.current = 'select_player_character'

    def random_button_clicked(self):
        shared.set_current_match("character_mode_str", "random")
        shared.set_current_format()
        self.manager.transition.direction = 'left'
        self.manager.current = 'match'
