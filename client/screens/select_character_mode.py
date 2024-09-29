from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file("client/layouts/select_character_mode.kv")

class SelectCharacterMode(MDScreen):
    def on_back_button_clicked(self):
        self.manager.current = 'select_gamemode'

    def pick_button_clicked(self):
        self.manager.current = 'select_character'

    def randoms_button_clicked(self):
        pass
        # self.manager.current = 'match_screen'
