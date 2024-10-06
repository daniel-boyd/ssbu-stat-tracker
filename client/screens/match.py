from .. import shared
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file("client/layouts/match.kv")

class Match(MDScreen):
    
    def on_pre_enter(self):
        player_1_label = self.ids.player_1_label
        player_2_label = self.ids.player_2_label
        player_1_label.text = shared.get_current_match_value_from_key("player_1")
        player_2_label.text = shared.get_current_match_value_from_key("player_2")
        player_1_label.text = "dnl"
        player_2_label.text = "cnl"

    def stage_button_clicked(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'stage_list'
