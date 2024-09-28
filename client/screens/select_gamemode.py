from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file("client/layouts/select_gamemode.kv")

class SelectPlayerCount(MDScreen):
    def on_back_button_clicked(self):
        self.manager.current = 'select_player_names'

    def standard_button_clicked(self):
        pass
        # self.manager.current = 'select_character_mode'

    def handicap_button_clicked(self):
        self.manager.current = 'select_character_mode'
