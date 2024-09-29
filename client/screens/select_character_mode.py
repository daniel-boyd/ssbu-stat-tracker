from .. import shared
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file("client/layouts/select_character_mode.kv")

class SelectCharacterMode(MDScreen):
    def on_back_button_clicked(self):
        self.manager.current = 'select_gamemode'

    def pick_button_clicked(self):
        shared.set_current_match("character_mode_str", "pick")
        shared.set_current_format()
        self.manager.current = 'select_player_character'

    def random_button_clicked(self):
        shared.set_current_match("character_mode_str", "random")
        shared.set_current_format()
        self.manager.current = 'match_screen'
