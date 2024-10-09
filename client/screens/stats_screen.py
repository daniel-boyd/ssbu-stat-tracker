from .. import shared
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDExtendedFabButton

Builder.load_file("client/layouts/stats_screen.kv")

class StatsScreen(MDScreen):

    def on_pre_enter(self):
        player_1_stats = self.ids.player_1_stats
        player_2_stats = self.ids.player_2_stats
        player_1_stats.text = shared.get_current_match_value_from_key("players")[1]
        player_2_stats.text = shared.get_current_match_value_from_key("players")[2]
        player_1_name = shared.get_current_match_value_from_key("players")[1]
        player_2_name = shared.get_current_match_value_from_key("players")[2]
        # Set player names?
        player_1_stats.txt = player_1_name
        player_2_stats.txt = player_2_name

        player_stocks = shared.get_current_match_value_from_key("player_stocks")
        player_1_stocks_taken = str(player_stocks.get(player_1_name,0))
        player_2_stocks_taken = str(player_stocks.get(player_2_name,0))
        self.ids.player_1_stocks_taken.text = player_1_stocks_taken
        self.ids.player_2_stocks_taken.text = player_2_stocks_taken

pass