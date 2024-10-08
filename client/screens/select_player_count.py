from .. import shared
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition

Builder.load_file("client/layouts/select_player_count.kv")

class SelectPlayerCount(MDScreen):
    def on_back_button_clicked(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_menu'

    def two_players_button_clicked(self):
        shared.set_current_match("num_players_str", "2p")
        shared.set_current_format()
        self.manager.get_screen('select_player_names').number_of_players = 2
        self.manager.transition.direction = 'left'
        self.manager.current = 'select_player_names'

    def three_players_button_clicked(self):
        shared.set_current_match("num_players_str", "3p")
        shared.set_current_format()
        self.manager.get_screen('select_player_names').number_of_players = 3
        self.manager.transition.direction = 'left'
        self.manager.current = 'select_player_names'
