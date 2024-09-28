from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file("client/layouts/select_player_count.kv")

class SelectPlayerCount(MDScreen):
    def on_back_button_clicked(self):
        self.manager.current = 'main_menu'

    def two_players_button_clicked(self):
        self.manager.get_screen('select_player_names').number_of_players = 2
        self.manager.current = 'select_player_names'

    def three_players_button_clicked(self):
        self.manager.get_screen('select_player_names').number_of_players = 3
        self.manager.current = 'select_player_names'
