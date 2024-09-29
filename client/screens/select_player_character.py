from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from .. import shared

Builder.load_file("client/layouts/select_player_character.kv")

class SelectPlayerCharacter(MDScreen):
    def on_back_button_clicked(self):
        self.manager.current = 'select_character_mode.kv'

    def player1_button_clicked(self):
            # shared.set_current_match("player_1", "character.png")
        self.manager.current = 'select_character'

    def player2_button_clicked(self):
            # shared.set_current_match("player_2", "character.png")
        self.manager.current = 'select_character'
